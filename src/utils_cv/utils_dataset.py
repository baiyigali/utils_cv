import os, re
import pandas as pd
import numpy as np


def get_td_dataset(csv_path, im_dir, sample_n=10):
    df = pd.read_csv(csv_path)

    filenames = df.drop_duplicates("filename")["filename"].tolist()
    np.random.seed(101)
    np.random.shuffle(filenames)
    filenames = filenames[:sample_n]
    df = df[df.filename.isin(filenames)]

    print("image", len(df.path.unique()))
    print("words", df.shape[0])
    df["path"] = df["filename"].apply(lambda x: os.path.join(im_dir, x))
    df["field_bbox"] = df["field_bbox"].apply(
        lambda x: np.array(re.sub("[\[\],]", " ", x).split(), np.float32).astype(
            np.int32
        )
    )
    return df


def get_tr_dataset(csv_path, image_dir, sample_n=1000):
    df = pd.read_csv(csv_path)
    df = df[(df.field_text != "nan") & (df.field_text != "!")]
    n = min(sample_n, df.shape[0])
    df = df.sample(n=n, random_state=1)

    df["field_text"] = df["field_text"].astype(str)
    df["path"] = df["filename"].apply(
        lambda x: os.path.join(image_dir, os.path.basename(x))
    )
    if "field_bbox" in df.keys():
        df["field_bbox"] = df["field_bbox"].apply(
            lambda x: np.array(
                re.sub("[\[\],]", " ", x).strip().split(), dtype=np.float32
            ).astype(np.int32)
        )

    return df
