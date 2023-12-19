
def get_formulation_details(user_symptoms):
    import pandas as pd
    import numpy as np

    symptoms = pd.read_csv("C:\\Users\\holla\\OneDrive\\Desktop\\ayurvedic_symptoms_desc.csv")
    FormulationClass = pd.read_csv("C:\\Users\\holla\\OneDrive\\Desktop\\FormulationClass.csv")
    df1 = pd.read_csv("C:\\Users\\holla\\Downloads\\medicine_-_Sheet1.csv")

        
    ## Making a list of all formulations/ RECIPE
    # ['Abhayarishta', 'Amritarishta', 'Aragvadharishta'...]
    formulations_lst = list(df1['Name of Medicine'])

    # making a list of main indications/ SYMPTOMS
    # original_list = ['Arsha, Agnimandya,\nUdararoga, Vibandha', 'SarvaJvara, Jirna Jvara'...]
    original_list = list(df1['Main Indications'])

    processed_list = []
    for item in original_list:
        # Remove spaces and newline characters, convert to lowercase
        # item = "   Process,  This,  String   " ==> processed_item =  process,this,string
        processed_item = ''.join(item.split()).lower()
        # ['arsha,agnimandya,udararoga,vibandha', 'sarvajvara,jirnajvara', ...]
        processed_list.append(processed_item)

        

    ## Finding all possible unique symptoms(Main indications)
    # List of lists of symptoms
    # ['arsha,agnimandya,udararoga,vibandha', 'sarvajvara,jirnajvara', ...]
    list_of_symptoms = processed_list

    # Flatten the list of lists and split the symptoms using commas and spaces
    # ["fever, headache", "cough, sore throat, fatigue",...] => [['fever', 'headache'], ['cough', 'sore', 'throat', 'fatigue']...]
    flat_symptoms = [symptom.replace(',', ' ').split() for symptoms in list_of_symptoms for symptom in symptoms.split(',')]

    # Get unique symptoms as a list
    #[['fever', 'headache'], ['cough', 'sore', 'throat', 'fatigue']...] => [one, two, three...]
    unique_symptoms = list(set(symptom for sublist in flat_symptoms for symptom in sublist))

    ## Making a dataset from the formulations & Main indication lists
    data = {
        "Formulation": formulations_lst,
        "Symptoms": processed_list,
    }

    # Create a DataFrame
    df = pd.DataFrame(data)
    # formulation  symptoms
    # f1           s1, s2, s3
    # f2           s1, s2, s3
    ## The symptom-Description Dataset
    symptoms['Symptom'] = symptoms['Symptom'].str.lower()

    # produces english name od symptom
    def symptoms_desc(symptom_name):
        row = symptoms[symptoms['Symptom'] == symptom_name.lower()]
        if not row.empty:
            description = row.iloc[0]['Description']
            ##3####### print(f'Description of "{symptom_name}": {description}')
        else:
            ######### print(f'Symptom "{symptom_name}" not found in the DataFrame.')
            pass
        
    # produces english of multiple symptoms at once
    def symptoms_lst_desc(user_symptoms):
        for item in user_symptoms:
            symptoms_desc(item)

        
    ## Spelling Correction
    import difflib
    # Your list of correct words (assuming you have a list called unique_symptoms)
    correct_words = unique_symptoms

    def correct_symptoms(symptoms):
        corrected_symptoms = []
        for symptom in symptoms:
            corrected_symptom = difflib.get_close_matches(symptom, correct_words, n=1, cutoff=0.6)
            if corrected_symptom:
                corrected_symptoms.append(corrected_symptom[0])
            else:
                corrected_symptoms.append(symptom)
        return corrected_symptoms


    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.naive_bayes import MultinomialNB

    import pandas as pd
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity

    # #  [java Agnimandy]
    # # user_input = input("Enter a list of symptoms separated by spaces: ")
    # # input_symptoms = user_input.split()

    # # user_symptoms => ['jara', 'agnimandya']
    user_symptoms_corrected = correct_symptoms(user_symptoms)
    for i in range(0,len(user_symptoms_corrected)):
        if user_symptoms_corrected[i]!=user_symptoms[i]:
            print(f"Did you mean: {user_symptoms_corrected[i].title()}?")
    
    
    

    symptoms_lst_desc(user_symptoms_corrected)
    # [java arsha] => jara arsha
    user_symptoms_str = " ".join(user_symptoms_corrected)  # Convert user symptoms to a single string
    # print(user_symptoms_str)
    # Create a DataFrame
    df = pd.DataFrame(data)





    # Create a TF-IDF vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # Fit and transform the symptom text data into numerical features
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['Symptoms'])

    # Transform user symptoms into TF-IDF format
    user_symptoms_tfidf = tfidf_vectorizer.transform([user_symptoms_str])

    # Calculate cosine similarity between user's symptoms and all formulations
    similarities = cosine_similarity(user_symptoms_tfidf, tfidf_matrix)


    # Set a threshold for similarity score (adjust as needed)
    similarity_threshold = 0.5  # You can adjust this value

    # Find all formulations with similarity scores above the threshold
    matching_indices = [i for i, sim in enumerate(similarities[0]) if sim > similarity_threshold]

    if not matching_indices:
        print("No matching formulations found for the provided symptoms.")
    else:
        # closest rows mein formulation column ka data
        # 130        Kasisadi Taila
        # 186    Arsho Kuthara Rasa
        closest_formulations = df.iloc[matching_indices]["Formulation"]

    #    print(closest_formulations.tolist())
        
        closest_formulations.tolist()
        ### Create a boolean mask to filter rows where the second column matches any element in closest_formulations
        mask = df1.iloc[:, 0].isin(closest_formulations)
        # Use the mask to select the rows that match the condition
        filtered_df = df1[mask]


        # Iterate through the filtered DataFrame and print each row separately
        diction = {}
        i=0
        for index, row in filtered_df.iterrows():
            key_name = user_symptoms_corrected[i]
            diction[key_name] = {'Name of Medicine':row['Name of Medicine'],
                                 "Vata":row['Vata'],
                                 "formulation": row['formulation']}
            i+=1
        print(diction)

            


get_formulation_details(user_symptoms=['vatavikara','arha'])

