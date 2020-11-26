"""The :mod:`cli` module allows for training 
and retraining of the project's machine learning model 
"""
# Author: Chris Dare
from datetime import datetime
from pathlib import Path
from typing import Optional

import joblib
import typer
from sklearn.metrics import classification_report

from firelord.model import train
from firelord.preprocess import get_training_dataset

DEFAULT_STORE = Path(__file__).parent.absolute() / ".store"


def main(
    model_folder_path: Optional[str] = DEFAULT_STORE,
    separating_date: Optional[str] = "2013-01-01",
):
    """Main serves as the entry point to train the machine learning model

    Parameters
    ----------
    separating_date: Optional[str], default = None
        separating_date: str, default=None
        The end of the training date range and beginning of the validation date. 


    """
    print("training model")

    model_folder_path = Path(model_folder_path).absolute()
    model_folder_path.mkdir(exist_ok=True)
    deployed_model_name = "ozai_latest_model.model"
    features = [
        "climate_vs",
        "climate_def",
        "climate_vap",
        "climate_aet",
        "precipitation",
        "landcover_5",
    ]
    training_data = get_training_dataset()
    date_split = "2013-01-01"
    train_ = training_data.loc[training_data.date < date_split]
    valid_ = training_data.loc[training_data.date > date_split]

    model = train(
        features=features, train_=train_, valid_=train_, target_col="burn_area"
    )
    predictions = model.predict(train_)
    metrics = classification_report(valid_, predictions)
    print(f"Finished training model \n {model} \n\n")
    print(f"Classification report available below \n {metrics}")
    print("Do you want to save this model? (Y/n)")
    trainer_decision = str(input()).strip().lower()
    if trainer_decision == "y":
        model_path = model_folder_path / f"{datetime.now():%Y_%m_%d}.model"
        joblib.dump(model, model_path)

        report_path = model_folder_path / f"{datetime.now():%Y_%m_%d}.report"
        report = open(report_path, "w")

        report.write(metrics)
        status = f"Model saved at {model_path}\nReport saved at {report_path}"
        print("Do you want deploy this model for use in predictions? (Y/n)")
        update_decision = str(input()).strip().lower()
        if update_decision == "y":
            deployed_model_path = model_folder_path / f"{deployed_model_name}.model"
            joblib.dump(model, deployed_model_path)
            status = f"{status}\n Model deployed at: {deployed_model_path}"
            deployed_model_report_path = (
                model_folder_path / f"{deployed_model_name}.report"
            )
            report = open(deployed_model_report_path, "w")
        else:
            status = f"{status}\n Production model not updated."

    else:
        status = "Model discarded."

    status = f"{status}\n Exiting."
    print(status)


if __name__ == "__main__":
    typer.run(main)
