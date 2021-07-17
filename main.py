import numpy as np
import pandas as pd
from NameEntityRecognition import get_entities_list
from PlacesAPI import get_location
from NameEntityRecognition import nlp_entities
from geopy.geocoders import Nominatim
import Location
from EnrichMetadata import get_metadata
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import classification_report

def main():
    print("This is the geolocation project. Welcome.\n")
    # read the data
    # df = pd.read_csv('~/Documents/geolocation/data/albertaT6.csv')
    # df_len = len(df)
    # list_of_coordinates = []
    # nom = Nominatim(user_agent="geolocation")
    # pred_latitude = []
    # pred_longitude = []
    # real_latitude = df['lat']
    # real_longitude = df['lon']
    # print("============================== Starting the search =========================")
    # for i in range(df_len):
    #     print(i)
    #     tweet_text = df['text'][i]
    #     tweet_id = str(df['id'][i])
    #     if len(nlp_entities(tweet_text)) > 0:
    #         print("There are entities")
    #         entity = nlp_entities(tweet_text)[0] # solo una entidad
    #         # query to get the coordinates and add them
    #         n = nom.geocode(entity)
    #         if n is not None:
    #             print("I found the coordinates")
    #             pred_latitude.append(n.latitude)
    #             pred_longitude.append(n.longitude)
    #         else:
    #             print("I didn't find the coordinates. I will try the metadata")
    #             if get_metadata(tweet_id) is not None:
    #                 pred_latitude.append(get_metadata(tweet_id)[0])
    #                 pred_longitude.append(get_metadata(tweet_id)[1])
    #             else:
    #                 # I dont know in this case what the coordinate is
    #                 print("I didn't find metadata either, return (0.0, 0.0)")
    #                 pred_latitude.append(0.00)
    #                 pred_longitude.append(0.00)
    #     else:
    #         # we call metadata
    #         print("There are no entities, I will see metadata")
    #         if get_metadata(tweet_id) is not None:
    #             print("I found metadata coordinates")
    #             pred_latitude.append(get_metadata(tweet_id)[0])
    #             pred_longitude.append(get_metadata(tweet_id)[1])
    #         else:
    #             print("I didn't find metadata. I will return (0.0, 0.0)")
    #             pred_latitude.append(0.00)
    #             pred_longitude.append(0.00)
    # print("============================== out of the searching =========================")
    # real_latitude = list(real_latitude)
    # real_longitude = list(real_longitude)
    # pred_latitude_file = open("pred_latitude.txt", "w")
    # real_latitude_file = open("real_latitude.txt", "w")
    # pred_longitude_file = open("pred_longitude.txt", "w")
    # real_longitude_file = open("real_longitude.txt", "w")
    # for element in pred_latitude:
    #     pred_latitude_file.write(f"{element} \n")
    # for element in real_latitude:
    #     real_latitude_file.write(f"{element}\n")
    #
    # for element in pred_longitude:
    #     pred_longitude_file.write(f"{element}\n")
    # for element in real_longitude:
    #     real_longitude_file.write(f"{element}\n")
    df_pred_latitude = pd.read_csv("./pred_latitude.txt", delimiter="\n")
    df_pred_longitude = pd.read_csv("./pred_longitude.txt", delimiter="\n")
    df_real_latitude = pd.read_csv("./real_latitude.txt", delimiter="\n")
    df_real_longitude = pd.read_csv("real_longitude.txt", delimiter="\n")
    print("====== Metrics ======")
    print(f"The f1 metric for the latitude prediction: {f1_score(np.floor(df_real_latitude).astype(int), np.floor(df_pred_latitude).astype(int), average='micro')}")
    print(f"The f1 metric for the longitude prediction: {f1_score(np.floor(df_real_longitude).astype(int), np.floor(df_pred_longitude).astype(int), average='micro')}")

    print(f"The precision metric for the latitude prediction: {precision_score(np.floor(df_real_latitude).astype(int), np.floor(df_pred_latitude).astype(int), average='micro')}")
    print(f"The precision metric for the longitude prediction: {f1_score(np.floor(df_real_longitude).astype(int), np.floor(df_pred_longitude).astype(int), average='micro')}")

    print(f"The recall metric for the latitude prediction: {recall_score(np.floor(df_real_latitude).astype(int), np.floor(df_pred_latitude).astype(int), average='micro')}")
    print(f"The recall metric for the longitude prediction: {recall_score(np.floor(df_real_longitude).astype(int), np.floor(df_pred_longitude).astype(int), average='micro')}")
    print("==== End Metrics ====")

if __name__ == "__main__":
    main()
