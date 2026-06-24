# Hotel Reservations Cancellation Prediction

## Project Overview

The **Hotel Reservations Cancellation Prediction** project aims to predict whether a hotel reservation will be canceled by analyzing various booking-related features. With the rapid growth of online hotel booking platforms, reservation cancellations have become a significant challenge for hotels, often leading to revenue loss and inefficient resource management.

Cancellations may occur due to changes in travel plans, scheduling conflicts, or the availability of free or low-cost cancellation options. This project leverages historical booking data to identify patterns associated with cancellations and build predictive models that can help hotels make informed decisions.

---

## Dataset Description

The dataset contains information about hotel reservations, customer demographics, booking details, and reservation outcomes.

### Data Dictionary

| Column Name | Description |
|------------|-------------|
| `Booking_ID` | Unique identifier for each booking |
| `no_of_adults` | Number of adults included in the reservation |
| `no_of_children` | Number of children included in the reservation |
| `no_of_weekend_nights` | Number of weekend nights (Saturday or Sunday) |
| `no_of_week_nights` | Number of weeknights (Monday to Friday) |
| `meal_type` | Meal plan selected by the customer |
| `required_car_parking_spaces` | Indicates whether parking space is required (`0` = No, `1` = Yes) |
| `lead_time` | Number of days between booking date and arrival date |
| `arrival_year` | Year of arrival |
| `arrival_month` | Month of arrival |
| `arrival_date` | Day of arrival |
| `market_segment` | Market segment through which the booking was made |
| `repeated_guest` | Indicates whether the customer is a returning guest (`0` = No, `1` = Yes) |
| `no_previous_cancellations` | Number of previous cancellations made by the customer |
| `previous_bookings_not_canceled` | Number of previous bookings successfully completed by the customer |
| `avg_price_per_room` | Average daily room price in Euros |
| `no_of_special_requests` | Number of special requests made by the customer |
| `booking_status` | Target variable indicating whether the booking was canceled or not |

---

## Exploratory Data Analysis (EDA) Findings

The exploratory data analysis revealed several important patterns related to reservation cancellations:

### 1. Guest Composition

- Reservations involving **two adults and no children** recorded the highest number of cancellations.
- Bookings that included children generally exhibited lower cancellation rates.

### 2. Booking Duration

- Reservations consisting primarily of **weeknight stays** experienced higher cancellation rates compared to weekend stays.
- Most bookings were made for weeknights.

### 3. Temporal Trends

- The year **2018** exhibited a higher cancellation rate than **2017**.
- The months of **July** and **October** recorded the highest number of cancellations.

### 4. Service Preferences

- Additional services selected during the reservation process had minimal influence on cancellation behavior.

### 5. Lead Time Analysis

- **Lead time** was identified as one of the most influential factors affecting cancellations.
- Reservations made closer to the arrival date were less likely to be canceled.
- Longer lead times significantly increased the probability of cancellation.

### 6. Market Segment Analysis

- Reservations made through **online travel platforms** exhibited the highest cancellation rates.
- This highlights the importance of maintaining a strong online presence and reputation.

---

## Machine Learning Models

Several classification algorithms were evaluated to predict reservation cancellations. Among the tested models:

| Model | Accuracy |
|--------|----------|
| Decision Tree Classifier | **85%** |

The **Decision Tree Classifier** achieved the highest accuracy of **85%**, making it the most effective model for this prediction task.

---

## Conclusion

This project successfully identified the key factors influencing hotel reservation cancellations. Features such as **lead time**, **market segment**, and **guest composition** played significant roles in determining cancellation behavior.

The findings can assist hotel management in:

- Optimizing reservation policies.
- Reducing cancellation rates.
- Improving revenue management strategies.
- Enhancing customer satisfaction.

By leveraging predictive analytics, hotels can proactively manage bookings and make data-driven operational decisions.

---

## Future Work

Potential future enhancements for this project include:

- Implementing advanced ensemble models such as **Random Forest**, **XGBoost**, and **LightGBM**.
- Deploying the predictive model as a web application.
- Integrating real-time reservation data for continuous prediction.
- Performing hyperparameter tuning to improve model performance.
