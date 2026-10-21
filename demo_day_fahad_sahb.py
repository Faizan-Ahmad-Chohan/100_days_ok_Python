from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
print(" here is  first NLP setup\n")


connotations=['hy, am good',
              'how the hell!',
              'how dare you',
              'it is a good day',
              'i love you',
              'i hate you',
              'he teaches good',
              'you are a lier'
              ]

              
label=[1,0,0,1,1,0,1,0]
pass_connotations=['bad connotations',
                   'good connotations'
                  ]

model = make_pipeline(TfidfVectorizer(), LogisticRegression())
model.fit(connotations, label)
continue_loop=True
while continue_loop:
    test_sentence =input( "give your sentence. let the computer tell connotaition : ")
    prediction = model.predict([test_sentence])[0]
    

    print(f"Text: '{test_sentence}' -> Result: {pass_connotations[prediction]}")
    breaker=input("do you want to continue 'y' , 'n' : ").lower()
    if breaker=='n':
        continue_loop=False