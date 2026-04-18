import os

DATA_ROOT_DIR = "../data"

# data/raw directory
RAW_ROOT_DIR = os.path.join(DATA_ROOT_DIR, "raw")
RAW_FILENAME = 'input.csv'
RAW_FILE_PATH = os.path.join(RAW_ROOT_DIR, RAW_FILENAME)

# download dataset
DOWNLOAD_OUTPUT_DIR = RAW_ROOT_DIR
DOWNLOAD_OUTPUT_PATH = RAW_FILE_PATH

# data preparation
PREPARED_ROOT_DIR = os.path.join(DATA_ROOT_DIR, "prepared")

## data preparation by pandas
PANDA_PREPARED_INPUT_PATH = RAW_FILE_PATH
PANDA_PREPARED_DIR = os.path.join(PREPARED_ROOT_DIR, "pandas")
PANDA_PREPARED_DATA_PATH = os.path.join(PANDA_PREPARED_DIR, "prepared_data.csv")
PANDA_PREPARED_DATA_PARQUET_PATH = os.path.join(PANDA_PREPARED_DIR, "prepared_data.parquet")
PANDA_LABEL_ENCODING_PATH = os.path.join(PANDA_PREPARED_DIR, "label_encoding.pkl")

## data preparation by spark
SPARK_PREPARED_INPUT_PATH = RAW_FILE_PATH
SPARK_PREPARED_DIR = os.path.join(PREPARED_ROOT_DIR, "spark")
SPARK_PREPARED_DATA_PATH = os.path.join(SPARK_PREPARED_DIR, "prepared_data.csv")
SPARK_PREPARED_DATA_PARQUET_PATH = os.path.join(SPARK_PREPARED_DIR, "prepared_data.parquet")
SPARK_INDEXER_MODEL_PATH = os.path.join(SPARK_PREPARED_DIR, "indexer_model")

# training
TRAINING_ROOT_DIR = os.path.join(DATA_ROOT_DIR, "models")
FEATURE_COLS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

## sklearn training
SKLEARN_TRAINING_INPUT_PATH = PANDA_PREPARED_DATA_PARQUET_PATH
SKLEARN_TRAINING_DIR = os.path.join(TRAINING_ROOT_DIR, "sklearn")
SKLEARN_SCALER_JOBLIB_PATH = os.path.join(SKLEARN_TRAINING_DIR, "scaler.joblib")
SKLEARN_MODEL_JOBLIB_PATH = os.path.join(SKLEARN_TRAINING_DIR, "model.joblib")
SKLEARN_MODEL_PICKLE_PATH = os.path.join(SKLEARN_TRAINING_DIR, "model.pkl")

## sklearn inference
INFERENCE_ROOT_DIR = os.path.join(DATA_ROOT_DIR, "inference")
INFERENCE_INPUT_DIR = os.path.join(INFERENCE_ROOT_DIR, "input")
INFERENCE_EXPECTED_DIR = os.path.join(INFERENCE_ROOT_DIR, "expected")

SKLEARN_INFERENCE_INPUT_PATH = os.path.join(INFERENCE_INPUT_DIR, "input.csv")
SKLEARN_INFERENCE_EXPECTED_PATH = os.path.join(INFERENCE_EXPECTED_DIR, "expected.csv")
SKLEARN_INFERENCE_DIR = os.path.join(INFERENCE_ROOT_DIR, "sklearn")
SKLEARN_INFERENCE_OUTPUT_PATH = os.path.join(SKLEARN_INFERENCE_DIR, "output_sklearn.csv")
SKLEARN_INFERENCE_MODEL_PICKLE_PATH = SKLEARN_MODEL_PICKLE_PATH
SKLEARN_INFERENCE_INPUT_LABEL_ENCODING_PATH = PANDA_LABEL_ENCODING_PATH
SKLEARN_INFERENCE_SCALER_JOBLIB_PATH = SKLEARN_SCALER_JOBLIB_PATH
