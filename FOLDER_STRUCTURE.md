# 📂 PyProjects - Folder Structure & File Locations Guide

---

## 📑 Quick Navigation

```
PyProjects/
├── README.md                          # Main repository documentation
├── FOLDER_STRUCTURE.md               # This file - complete folder guide
├── requirements.txt                  # Python dependencies
├── .gitignore
│
├── 📁 core/                          # Main projects directory
│   ├── FoodOrderDashboard/
│   │   ├── README.md                # Project overview & documentation
│   │   ├── app.py                   # Main application file
│   │   ├── requirements.txt          # Project-specific dependencies
│   │   ├── config/                  # Configuration files
│   │   ├── templates/               # HTML templates
│   │   ├── static/                  # CSS, JS, images
│   │   ├── data/                    # Local project data
│   │   ├── models/                  # Project ML models
│   │   └── utils/                   # Helper functions
│   │
│   └── (Other core projects to be added)
│
├── 📁 notebooks/                     # Jupyter Notebook experiments
│   ├── 01_Python_Basics/
│   │   ├── Introduction.ipynb
│   │   ├── Data_Types.ipynb
│   │   ├── Functions_and_OOP.ipynb
│   │   └── Problem_Solving.ipynb
│   │
│   ├── 02_Data_Science/
│   │   ├── NumPy_Fundamentals.ipynb
│   │   ├── Pandas_DataFrames.ipynb
│   │   ├── Data_Cleaning.ipynb
│   │   ├── Data_Visualization.ipynb
│   │   └── Statistical_Analysis.ipynb
│   │
│   ├── 03_Machine_Learning/
│   │   ├── Regression_Models.ipynb
│   │   ├── Classification_Algorithms.ipynb
│   │   ├── Clustering_Techniques.ipynb
│   │   ├── Model_Evaluation.ipynb
│   │   ├── Feature_Engineering.ipynb
│   │   └── Hyperparameter_Tuning.ipynb
│   │
│   ├── 04_Deep_Learning/
│   │   ├── Neural_Networks_Basics.ipynb
│   │   ├── TensorFlow_Keras.ipynb
│   │   ├── CNN_Computer_Vision.ipynb
│   │   ├── RNN_LSTM.ipynb
│   │   ├── PyTorch_Intro.ipynb
│   │   └── Transfer_Learning.ipynb
│   │
│   └── 05_Projects/
│       ├── End_to_End_ML_Project.ipynb
│       ├── Image_Classification.ipynb
│       ├── Time_Series_Forecasting.ipynb
│       └── NLP_Sentiment_Analysis.ipynb
│
├── 📁 scripts/                       # Python utility scripts
│   ├── utils/
│   │   ├── data_processor.py        # Data preprocessing utilities
│   │   ├── model_utils.py           # Model training helpers
│   │   ├── visualization.py         # Plotting & visualization
│   │   └── config.py                # Configuration management
│   │
│   ├── data_scripts/
│   │   ├── download_datasets.py     # Dataset downloading
│   │   ├── clean_data.py            # Data cleaning scripts
│   │   └── feature_engineering.py   # Feature creation
│   │
│   ├── ml_scripts/
│   │   ├── train_model.py           # Model training script
│   │   ├── evaluate_model.py        # Model evaluation
│   │   ├── predict.py               # Make predictions
│   │   └── hyperparameter_tune.py   # Hyperparameter optimization
│   │
│   └── dl_scripts/
│       ├── train_neural_net.py      # Neural network training
│       ├── prepare_images.py        # Image preprocessing
│       └── inference.py             # Model inference
│
├── 📁 data/                          # Datasets & data files
│   ├── raw/                         # Raw datasets
│   │   ├── dataset1.csv
│   │   ├── dataset2.json
│   │   └── images/
│   │
│   ├── processed/                   # Cleaned & processed data
│   │   ├── train_data.csv
│   │   ├── test_data.csv
│   │   └── validation_data.csv
│   │
│   └── external/                    # External data sources
│       └── README.md                # Data source documentation
│
├── 📁 models/                        # Trained models & weights
│   ├── ml_models/
│   │   ├── random_forest.pkl
│   │   ├── logistic_regression.pkl
│   │   └── svm_classifier.pkl
│   │
│   ├── dl_models/
│   │   ├── cnn_model.h5            # Keras model
│   │   ├── bert_model.pt           # PyTorch model
│   │   └── model_weights/          # Model weight files
│   │
│   └── model_registry.json         # Model metadata & versions
│
├── 📁 TODO/                          # Templates & starter projects
│   ├── README.md                    # Flask Web App Starter docs
│   ├── flask_app.py                 # Flask template
│   ├── requirements.txt              # Flask dependencies
│   ├── templates/
│   │   ├── index.html
│   │   └── base.html
│   │
│   └── static/
│       ├── style.css
│       └── script.js
│
├── 📁 docs/                          # Documentation & learning notes
│   ├── CONCEPTS.md                  # Core concept explanations
│   ├── ALGORITHMS.md                # Algorithm references
│   ├── BEST_PRACTICES.md            # Coding best practices
│   ├── TROUBLESHOOTING.md           # Common issues & solutions
│   │
│   ├── python/
│   │   ├── fundamentals.md
│   │   ├── oop_guide.md
│   │   └── advanced_concepts.md
│   │
│   ├── ml/
│   │   ├── regression_guide.md
│   │   ├── classification_guide.md
│   │   ├── clustering_guide.md
│   │   └── model_evaluation.md
│   │
│   ├── dl/
│   │   ├── neural_networks.md
│   │   ├── cnn_guide.md
│   │   ├── rnn_guide.md
│   │   └── transfer_learning.md
│   │
│   └── datasets/
│       ├── available_datasets.md
│       └── data_sources.md
│
└── 📁 tests/                         # Unit tests (optional)
    ├── test_utils.py
    ├── test_models.py
    └── test_scripts.py
```

---

## 📍 File Locations Reference

### Core Project Files
| File/Folder | Location | Description |
|------------|----------|-------------|
| Main README | `/README.md` | Repository overview & setup instructions |
| Folder Guide | `/FOLDER_STRUCTURE.md` | This comprehensive guide |
| Requirements | `/requirements.txt` | Main project dependencies |
| Food Dashboard | `/core/FoodOrderDashboard/` | Real-world dashboard project |
| Dashboard Docs | `/core/FoodOrderDashboard/README.md` | Project-specific documentation |

### Notebooks by Category
| Category | Location | Files |
|----------|----------|-------|
| Python Basics | `/notebooks/01_Python_Basics/` | 4 notebooks |
| Data Science | `/notebooks/02_Data_Science/` | 5 notebooks |
| Machine Learning | `/notebooks/03_Machine_Learning/` | 6 notebooks |
| Deep Learning | `/notebooks/04_Deep_Learning/` | 6 notebooks |
| Projects | `/notebooks/05_Projects/` | 4 notebooks |

### Scripts Organization
| Category | Location | Purpose |
|----------|----------|---------|
| Utils | `/scripts/utils/` | General utilities & config |
| Data Processing | `/scripts/data_scripts/` | Data handling & engineering |
| ML Scripts | `/scripts/ml_scripts/` | Model training & evaluation |
| DL Scripts | `/scripts/dl_scripts/` | Neural network & deep learning |

### Data Directory
| Subdirectory | Location | Content |
|--------------|----------|---------|
| Raw Data | `/data/raw/` | Original datasets |
| Processed Data | `/data/processed/` | Cleaned datasets |
| External Data | `/data/external/` | Third-party data sources |

### Models Storage
| Category | Location | Format |
|----------|----------|--------|
| ML Models | `/models/ml_models/` | .pkl, .joblib |
| DL Models | `/models/dl_models/` | .h5, .pt, .pth, .pb |
| Model Metadata | `/models/model_registry.json` | JSON registry |

### Documentation
| Category | Location | Content |
|----------|----------|---------|
| Concepts | `/docs/CONCEPTS.md` | Core theories & concepts |
| Algorithms | `/docs/ALGORITHMS.md` | Algorithm references |
| Python Docs | `/docs/python/` | Python-specific guides |
| ML Docs | `/docs/ml/` | Machine learning guides |
| DL Docs | `/docs/dl/` | Deep learning guides |
| Datasets | `/docs/datasets/` | Data source information |

---

## 🚀 Quick File Access

### To work with different topics:

**Python Basics:**
- Notebooks: `/notebooks/01_Python_Basics/`
- Scripts: `/scripts/utils/`
- Docs: `/docs/python/`

**Data Science:**
- Notebooks: `/notebooks/02_Data_Science/`
- Scripts: `/scripts/data_scripts/`
- Data: `/data/`
- Docs: `/docs/ml/`

**Machine Learning:**
- Notebooks: `/notebooks/03_Machine_Learning/`
- Scripts: `/scripts/ml_scripts/`
- Models: `/models/ml_models/`
- Docs: `/docs/ml/`

**Deep Learning:**
- Notebooks: `/notebooks/04_Deep_Learning/`
- Scripts: `/scripts/dl_scripts/`
- Models: `/models/dl_models/`
- Docs: `/docs/dl/`

**Projects:**
- End-to-End Projects: `/notebooks/05_Projects/`
- Production Projects: `/core/`
- Templates: `/TODO/`

---

## 📝 How to Use This Guide

1. **Finding a specific topic?** → Check the Quick Navigation at the top
2. **Looking for file locations?** → Use the File Locations Reference tables
3. **Want to work on a category?** → Navigate to Quick File Access
4. **Need to understand structure?** → Review the folder tree

---

## 🔄 Repository Growth

As the repository grows:
- New notebooks will be added to `/notebooks/`
- Project files will expand in `/core/`
- New scripts will be organized in `/scripts/`
- Models will be saved in `/models/`
- Documentation will grow in `/docs/`

---

## 📌 Tips

✅ Always check **README.md** in each folder for specific instructions  
✅ Use **requirements.txt** to install necessary dependencies  
✅ Check `/docs/` for concept explanations before diving into notebooks  
✅ Models are organized by type (ML vs DL)  
✅ All notebooks are self-contained with markdown explanations  

---

**Last Updated:** April 25, 2026  
**Repository:** dpk45deepak/PyProjects
