# **Building a Modern Smart Claims Platform on Databricks**

Link to Medium Series: https://medium.com/@zekiemretekin/building-a-modern-smart-claims-platform-on-databricks-architecture-use-case-part-1-370220fceed9?postPublishedType=initial 

![](https://miro.medium.com/v2/resize:fit:1400/1*zhvU0-sLPr9cIGhgdJkSsQ.png)

Source: Databricks Website

In the current data landscape, “end-to-end” often just means moving data from point A to point B. But a true production-grade platform needs to go further: from ingestion and governance to machine learning and a user-facing application layer.

This series documents the build of a complete **Smart Claims** system for a car insurance provider. We aren’t just building pipelines; we are building a fully integrated Lakehouse solution that ingests telematics, processes claims via Computer Vision, and serves insights through a custom-built front end.

We will be leveraging the latest capabilities of the **Databricks Intelligence Platform**, specifically focusing on:

- **Lakeflow Connect & Declarative Pipelines** for robust ingestion and ETL.
- **Mosaic AI & MLflow** to train and manage computer vision models.
- **Databricks Apps** to host the user-facing portal directly on the platform.
- **Databricks Genie** for natural language analytics.

This is Part 1 of a 7-part series. Here, we define the architecture, the specific business problems we are solving, and the final application logic.

# **The Business Problem: Automating Insurance Claims**

For this project, we are simulating a car insurance provider struggling with two common bottlenecks: **fragmented data**and **manual verification**.

Currently, when a customer submits a crash claim, a human agent must manually cross-reference policy documents, check driver history, and visually inspect photos of the damage. This is slow, error-prone, and expensive.

# **Our Solution Goals**

We are building a “Single Source of Truth” within Databricks that automates this workflow:

1. **Unified Data Estate:** Consolidating customer info, claims history, active policies, and live telematics (IoT data from vehicles) into one governed Lakehouse.
2. **Automated Verification:**
- **Speed Check:** Did the telematics data indicate speeding at the time of the crash?
- **Policy Check:** Is the driver eligible for a refund under their current terms?
- **Damage Validation:** Does the user’s description of the “minor scratch” actually match the image they uploaded? (We will use a custom Computer Vision model to classify severity).

# **The Technical Architecture**

To achieve this, we are deploying a standard Medallion Architecture (Bronze/Silver/Gold) populated by three distinct ingestion patterns.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:1400/1*I8jTTx5KTt7E_CNxuY46bA.png)

### **1. Ingestion Layer**

We will handle multi-modal data ingestion:

- **SQL Server:** Holds structured transactional data (Customer Profiles, Policies, Claims History). We will ingest this using **Lakeflow Connect**.
- **Kinesis Data Streams:** Provides high-velocity telematics data from vehicles.
- **Amazon S3 (Object Storage):** Serves as the landing zone for unstructured data, specifically the images of car crashes uploaded by users.

### **2. Processing & Transformation (The Medallion Layer)**

We will create a catalog `smart_claims_dev` containing four schemas:

- `landing`: The initial drop zone for raw files.
- `raw` (Bronze): The ingested data, cleaned slightly but preserving history.
- `silver`: Data with quality checks applied. This is where we filter out invalid records and standardize formats.
- `gold`: Aggregated, business-ready data joined for reporting.

We will use **Lakeflow Declarative Pipelines** to orchestrate these transformations, ensuring we have a resilient, maintainable code base rather than a web of fragile scripts.

### **3. The Intelligence Layer**

Once the data is refined, we apply intelligence:

- **Mosaic AI:** We will train a Machine Learning model to analyze crash images and classify them by severity (e.g., Light, Moderate, Severe).
- **MLflow:** Used for experiment tracking, model registry, and serving the model via an endpoint.

### **4. The Consumption Layer**

Data is useless if it sits in a silo. We will expose our insights via:

- **SQL Warehouses & AI/BI Dashboards:** For standard executive reporting.
- **Databricks Genie:** Allowing non-technical stakeholders to query data using natural language.
- **Databricks Apps:** A custom Python-based web application hosting the Customer Portal and Admin Console.

# **The End Product: What We Are Building**

By the end of this series, we will have a deployed **Databricks App** that serves as the entry point for the entire workflow.

### **1. The Customer View**

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:1400/1*wgI1A9LBAVaTFJ7KH7JkWg.png)

Landing Page to Submit the Claim

The app provides a frontend for policyholders to submit a claim. They upload an image of the crash, enter details (collision type, number of vehicles), and self-assess the damage.

Behind the scenes, the system triggers the ML model. It compares the model’s prediction against the user’s self-assessment. If the telematics show the driver was driving safely, the policy is valid, and the ML model confirms the damage description, the system **automatically approves** the refund in real-time.

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:1400/1*LVa-dKuEbgmTEKqxCfuJtg.png)

Claim Analysis Results

### **2. The Admin View**

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:1400/1*Fq9UjkjOk1-RRyQ0Mlv04Q.png)

Admin View for All Existing Claims

For claims that fail these automated checks (e.g., the user claims “minor scratch” but the image shows a “totaled” bumper), the claim is flagged.

We will build an Admin Console where internal auditors can:

- Review flagged claims.
- See the side-by-side comparison of User vs. AI classification.
- Filter claims by severity or financial impact.
- Drill down into customer history (powered by **Lakebase** for low-latency retrieval).

Press enter or click to view image in full size

![](https://miro.medium.com/v2/resize:fit:1400/1*jhiN7W4j3Uijkfr5YZzZcw.png)

Detailed View of a Single Claim
