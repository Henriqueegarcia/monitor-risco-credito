1. Título e DescriçãoMonitor de Risco de Crédito — Pipeline End-to-End & Modelo PreditivoPipeline automatizado para monitorar e prever a inadimplência no sistema financeiro nacional. Consome dados do Banco Central (SCR.data) e indicadores macroeconômicos (API SGS), organiza em camadas Medallion (Bronze/Silver/Gold) e alimenta um modelo preditivo com dashboard Real vs. Previsto.

2. Arquitetura (Rascunho)Plaintext[ BCB: SCR.data + API SGS ] ──► [ Bronze (Raw) ] ──► [ Silver (Clean & Dimensional) ] ──► [ Gold (Datamarts & Features) ] ──► [ MLflow / LightGBM ] ──► [ Dashboard AI/BI ]

3. StackPlataforma: Databricks Free Edition.Processamento: PySpark + Delta Lake.Transformação e Modelagem: dbt (dbt-databricks).Orquestração: Databricks Workflows (Airflow como extra).Machine Learning & Tracking: LightGBM + MLflow.Visualização: Databricks AI/BI (ou Power BI).Qualidade e Testes: dbt tests + pytest.Engenharia de Software: Git/GitHub, Docker, GitHub Actions.

4. Status
   Semana 1: Ingestão e Camada Bronze[ ] Ingerir SCR.data e API SGS via PySpark e salvar no Delta Lake.
   Semana 2: Camada Silver e Modelagem Dimensional[ ] Tratar tipos e construir modelagem dimensional (Star Schema).
   Semana 3: Camada Gold, dbt e Engenharia de Features[ ] Criar datamarts e Feature Store com dbt e testes de schema.
   Semana 4: Carga Incremental[ ] Ajustar pipeline para carga mensal incremental com defasagem de 30 dias.
   Semana 5: Treinamento, MLflow e Servimento[ ] Treinar LightGBM, registrar no MLflow e gerar previsões de inadimplência.
   Semana 6: Visualização[ ] Construir dashboard Real vs. Previsto no Databricks AI/BI.
   Semana 7: Orquestração e CI/CD[ ] Encadear pipeline no Databricks Workflows e configurar GitHub Actions.
   Semana 8: Polimento e Portfólio[ ] Documentar README e estruturar storytelling para entrevistas.5.


   Diário de BordoSemanaO que fizO que aprendiO que travouSemana 1Semana 2Semana 3Semana 4Semana 5Semana 6Semana 7Semana 8
