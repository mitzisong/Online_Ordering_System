import models
import csv
from datetime import datetime

def load_products(session):
    # use u.user
    #open a file
    with open('seed_data/flavors.csv', "rU") as f:
        #read file
        reader = csv.reader(f)
        #parse a line
        for row in reader:
            #create object
            product = models.Product(id=row[0], 
                                     flavor=row[1], 
                                     size=row[2], 
                                     cost=row[3], 
                                     quantity=row[4],
                                     description=row[5])

            #add object to a session
            session.add(product)
        #commit to a session
        session.commit()


def main(session):
    # You'll call each of the load_* functions with the session as an argument
    load_products(session)

    

if __name__ == "__main__":
    main(models.session)
