import pickle

talabalar1={'ism':'asror', 'familya':'abdurazoqov', 'tyil':2000, 'kurs':2}
talabalar2={'ism':'asilbek', 'familya':'abdurazoqov', 'tyil':2001, 'kurs':1}

filename= 'info.pkl'
with open(filename,'wb') as file:
    pickle.dump(talabalar1,file)
    pickle.dump(talabalar2,file)
