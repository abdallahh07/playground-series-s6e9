<!-- ════════════════ HEADER ════════════════ -->
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=210&color=0:1F283E,50:2B3653,100:1F283E&text=Abdallah%20Hashad&fontColor=F4F4F4&fontSize=52&fontAlignY=36&desc=Quantitative%20Finance%20%C3%97%20Machine%20Learning&descColor=EDCC80&descAlignY=58&descSize=18&animation=fadeIn" width="100%" />

<!-- typing effect -->
<a href="https://github.com/abdallahh07">
<img src="https://readme-typing-svg.demolab.com?font=Space+Grotesk&weight=600&size=24&duration=2800&pause=900&color=EDCC80&center=true&vCenter=true&width=620&lines=Machine+Learning+Engineer;Data+Scientist;CFA-level+Valuation+meets+Modern+ML;Building+models+that+answer+economic+questions" alt="Typing intro" />
</a>

<br/>

<img src="https://komarev.com/ghpvc/?username=abdallahh07&style=for-the-badge&color=2B3653&label=PROFILE+VIEWS" alt="Profile views" />

</div>

---

## <img src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif" width="30"> About me

```python
class AbdallahHashad:
    role        = "Machine Learning Engineer & Data Scientist"
    location    = "Cairo, Egypt 🇪🇬"
    edge        = "CFA-level valuation + DCF modelling + professional appraisal work"

    def building(self):
        return ["end-to-end ML pipelines", "leakage-proof feature engineering",
                "tuned gradient boosting models", "quantitative finance tooling"]

    def current_focus(self):
        return {"learning": ["Hands-On ML (Géron)", "Linear Algebra (Strang)", "SQL"],
                "goal": "models that answer real economic questions, not just minimise loss"}
```

🌐 **Portfolio:** [abdallah-hashad.vercel.app](https://portfolio-rho-three-v6f18jwj5o.vercel.app) &nbsp;•&nbsp; 📊 **Kaggle:** [abdallahhashad0](https://www.kaggle.com/abdallahhashad0) &nbsp;•&nbsp; ✍️ **Medium:** [@abdallahhashad029](https://medium.com/@abdallahhashad029)

---

# Playground Series S6E9 — EV Purchase Prediction

Kaggle Playground Series (Season 6, Episode 9): binary classification predicting whether
a consumer will buy an electric vehicle (`Will_Buy_EV`), using features inspired by the
[EV Adoption Behavior and Range Anxiety dataset](https://www.kaggle.com/datasets/itzzomkar/ev-adoption-behavior-and-range-anxiety).

## Status

Project structure scaffolded. EDA and modeling not yet started.

## Data

`train.csv`, `test.csv`, and `sample_submission.csv` from the competition, kept locally
under `data/raw/` and excluded from version control (`train.csv` is too large for git).

Features: `Age`, `Annual_Income_USD`, `Daily_Commute_km`, `Number_of_Cars_Owned`,
`Charging_Stations_Near_Home`, `Charging_Stations_Near_Work`, `Environmental_Concern_Level`,
`Gender`, `City_Type`, `Current_Car_Type`, `Home_Charging_Possible`, `Subsidy_Available`,
`Range_Anxiety_Level`. Target: `Will_Buy_EV`.

## Structure

```
├── config/           # config.yml — paths, feature lists, model params
├── data/raw/          # train.csv, test.csv, sample_submission.csv (not tracked)
├── notebooks/         # EDA and experimentation
├── processing/        # data loading and feature engineering
├── charts/            # saved EDA/model plots
├── trained_model/      # saved model artifacts
├── submissions/        # generated Kaggle submissions
├── app/               # FastAPI serving layer
├── pipeline.py         # sklearn Pipeline definition
├── train_pipeline.py   # training entry point
└── predict.py          # scoring / submission generation
```

## Setup

```bash
pip install -r requirements.txt
```
