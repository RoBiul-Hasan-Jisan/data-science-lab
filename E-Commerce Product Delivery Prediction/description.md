# E-Commerce Product Delivery Prediction

## Project Overview

With the rapid growth of e-commerce, ensuring timely product delivery has become a critical factor in customer satisfaction and business success. Delayed deliveries can negatively impact customer trust, increase operational costs, and reduce repeat purchases. Therefore, accurately predicting delivery outcomes enables companies to take proactive measures to improve logistics efficiency and enhance customer experience.

The objective of this project is to develop a machine learning-based predictive system capable of determining whether an e-commerce product will be delivered on time. In addition to building predictive models, the project investigates the key factors influencing delivery performance and analyzes customer purchasing behavior. Through exploratory data analysis, feature engineering, and model evaluation, valuable insights are extracted to support data-driven decision-making within the logistics and supply chain process.

The dataset consists of 10,999 shipment records collected from an international e-commerce company specializing in electronic products. Various shipment, product, and customer-related attributes were analyzed to identify patterns associated with delivery success and delays.

---

## Data Dictionary

| Variable            | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| ID                  | Unique customer identification number                         |
| Warehouse_block     | Warehouse block from which the product was dispatched         |
| Mode_of_Shipment    | Transportation method used for shipment (Ship, Flight, Road)  |
| Customer_care_calls | Number of customer service calls regarding shipment status    |
| Customer_rating     | Customer satisfaction rating ranging from 1 to 5              |
| Cost_of_the_Product | Product cost in US Dollars                                    |
| Prior_purchases     | Number of previous purchases made by the customer             |
| Product_importance  | Importance level of the product (Low, Medium, High)           |
| Gender              | Customer gender                                               |
| Discount_offered    | Discount percentage offered on the product                    |
| Weight_in_gms       | Product weight in grams                                       |
| Reached.on.Time_Y.N | Target variable (0 = Delivered on Time, 1 = Delayed Delivery) |

---

## Key Findings from Exploratory Data Analysis

The exploratory data analysis revealed several important relationships between product characteristics, customer behavior, and delivery outcomes.

### Product Characteristics

* Product weight was identified as one of the most influential factors affecting delivery performance.
* Products weighing between **2,500 and 3,500 grams** showed a higher probability of being delivered on schedule.
* Lower-cost products, particularly those priced below **$250**, demonstrated better delivery performance compared to higher-priced items.
* Most shipments originated from **Warehouse F**, indicating that this warehouse serves as a major distribution hub for the company.

### Customer Behavior Analysis

* Customers who contacted customer support more frequently were more likely to experience delivery delays.
* A positive relationship was observed between prior purchases and successful deliveries, suggesting that satisfied customers tend to make repeat purchases.
* Customer ratings showed relatively limited influence on delivery outcomes compared to shipment-related variables.
* Products offered with discounts greater than **10%** displayed a higher proportion of on-time deliveries, while products with minimal discounts were associated with more delivery delays.

### Shipment Analysis

* The majority of products were transported via ship, highlighting the company's reliance on maritime logistics.
* Shipment mode contributed to variations in delivery performance, although its impact was less significant than product weight and customer interaction metrics.

---

## Machine Learning Model Performance

Several classification algorithms were trained and evaluated to predict delivery status. Model performance was assessed using classification accuracy.

| Model                     | Accuracy |
| ------------------------- | -------- |
| Decision Tree Classifier  | 69%      |
| Random Forest Classifier  | 68%      |
| Logistic Regression       | 67%      |
| K-Nearest Neighbors (KNN) | 65%      |

Among all evaluated models, the **Decision Tree Classifier** achieved the highest prediction accuracy of **69%**, making it the best-performing model for this dataset. Random Forest and Logistic Regression produced competitive results, while KNN demonstrated comparatively lower predictive capability.

---

## Conclusion

This project successfully demonstrated the application of machine learning techniques in predicting e-commerce delivery performance. Through comprehensive exploratory data analysis and predictive modeling, several critical factors influencing delivery outcomes were identified.

The findings indicate that product weight, product cost, customer service interactions, prior purchase history, and discount offerings significantly affect the likelihood of timely delivery. Customers with frequent support inquiries were more likely to experience delays, whereas customers with a strong purchase history generally received products on time and continued to engage with the platform.

From a predictive modeling perspective, the Decision Tree Classifier achieved the best overall performance with an accuracy of 69%, highlighting its effectiveness in capturing complex decision patterns within the dataset. Although the achieved accuracy suggests room for improvement, the model provides valuable insights that can support logistics planning, risk assessment, and customer service optimization.

Future enhancements may include advanced feature engineering, hyperparameter optimization, handling class imbalance, and the implementation of more sophisticated ensemble learning techniques such as XGBoost, LightGBM, and CatBoost. Incorporating real-time shipment tracking data and external factors such as weather conditions, holidays, and geographical constraints could further improve predictive accuracy and business value.

Overall, this project demonstrates how data analytics and machine learning can be leveraged to improve supply chain efficiency, reduce delivery delays, and enhance customer satisfaction in the rapidly growing e-commerce industry.
