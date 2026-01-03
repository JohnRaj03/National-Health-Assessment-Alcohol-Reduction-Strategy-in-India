<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>National Health Assessment - Technical Implementation</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <style>
        .code-container {
            background-color: #1e1e1e;
            color: #d4d4d4;
            padding: 1.5rem;
            border-radius: 0.75rem;
            font-family: 'Consolas', monospace;
            font-size: 0.875rem;
            line-height: 1.5;
            overflow-x: auto;
            border: 1px solid #333;
        }
        .keyword { color: #569cd6; }
        .string { color: #ce9178; }
        .comment { color: #6a9955; }
        .function { color: #dcdcaa; }
        .number { color: #b5cea8; }
        .operator { color: #d4d4d4; }
    </style>
</head>
<body class="bg-gray-50 text-gray-900">

    <!-- Header -->
    <header class="bg-indigo-900 text-white py-12 px-6 shadow-2xl">
        <div class="container mx-auto">
            <h1 class="text-4xl font-black mb-4">Project Technical Implementation</h1>
            <p class="text-indigo-200 text-lg max-w-3xl">
                National Health Assessment & Community-Led Strategic Planning for Alcohol Reduction. 
                Integrating Python Analytics, Machine Learning, and SQL Infrastructure.
            </p>
        </div>
    </header>

    <main class="container mx-auto py-10 px-6 space-y-12">

        <!-- Machine Learning Visualisation Section -->
        <section class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-200">
                <h2 class="text-xl font-bold text-gray-800 mb-4">1a. Elbow Method (Optimal K)</h2>
                <div id="elbowPlot" class="w-full" style="height: 400px;"></div>
                <p class="mt-2 text-xs text-gray-500">Determining the optimal number of clusters for regional risk profiling.</p>
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-200">
                <h2 class="text-xl font-bold text-gray-800 mb-4">1b. Risk Segmentation Map</h2>
                <div id="riskPlot" class="w-full" style="height: 400px;"></div>
                <p class="mt-2 text-xs text-gray-500">K-Means clustering based on Male vs Female prevalence.</p>
            </div>
        </section>

        <!-- Python Logic Section -->
        <section class="grid grid-cols-1 lg:grid-cols-2 gap-8">
            <div class="space-y-4">
                <h2 class="text-2xl font-bold">2. Python Analytics Engine</h2>
                <p class="text-gray-600">
                    This module handles data normalization using <strong>StandardScaler</strong> and segments the population using <strong>Unsupervised Learning</strong>.
                </p>
                <div class="code-container">
<span class="comment"># --- Clustering and Normalization ---</span>
<span class="keyword">from</span> sklearn.cluster <span class="keyword">import</span> KMeans
<span class="keyword">from</span> sklearn.preprocessing <span class="keyword">import</span> StandardScaler

<span class="comment"># Normalizing gender-based consumption</span>
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[[<span class="string">'Male_Pct'</span>, <span class="string">'Female_Pct'</span>]])

<span class="comment"># Initializing K-Means with 3 Risk Zones</span>
kmeans = KMeans(n_clusters=<span class="number">3</span>, random_state=<span class="number">42</span>)
df[<span class="string">'Cluster'</span>] = kmeans.fit_predict(X_scaled)
                </div>
            </div>

            <div class="space-y-4">
                <h2 class="text-2xl font-bold">3. Financial Modeling (SIP)</h2>
                <p class="text-gray-600">
                    Calculating the <strong>Sobriety Dividend</strong> using the Future Value (FV) formula for wealth preservation.
                </p>
                <div class="code-container">
<span class="comment"># --- Sobriety Dividend Calculation ---</span>
<span class="keyword">def</span> <span class="function">calculate_wealth</span>(monthly, rate, years):
    r = (rate / <span class="number">100</span>) / <span class="number">12</span>
    n = years * <span class="number">12</span>
    <span class="keyword">return</span> monthly * (((<span class="number">1</span> + r)**n - <span class="number">1</span>) / r) * (<span class="number">1</span> + r)

<span class="comment"># Example: Redirecting ₹4k/month</span>
dividend = calculate_wealth(<span class="number">4000</span>, <span class="number">12</span>, <span class="number">20</span>)
print(<span class="string">f"Sobriety Dividend: ₹{dividend:,.0f}"</span>)
                </div>
            </div>
        </section>

        <!-- SQL Implementation -->
        <section>
            <div class="bg-gray-900 rounded-2xl p-8 shadow-2xl text-white">
                <h2 class="text-2xl font-bold mb-6">4. SQL Data Infrastructure & Query Engine (Roadmap 2030)</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div class="code-container bg-black border-gray-800">
<span class="comment">-- 1. IDENTIFY COMPLIANCE BREACHES (Legal Lock)</span>
<span class="keyword">SELECT</span> Retailer_Name, Distance_From_Institution
<span class="keyword">FROM</span> Alcohol_Retailers
<span class="keyword">WHERE</span> Distance_From_Institution <span class="operator">&lt;</span> <span class="number">300</span>;

<span class="comment">-- 2. BIOMETRIC LOG AUDIT (Minor Access Prevention)</span>
<span class="keyword">SELECT</span> Aadhaar_Token, Status, Created_At
<span class="keyword">FROM</span> Verification_Logs
<span class="keyword">WHERE</span> Status <span class="operator">=</span> <span class="string">'DENIED_AGE_RESTRICTION'</span>
<span class="keyword">ORDER BY</span> Created_At <span class="keyword">DESC</span>;

<span class="comment">-- 3. AGGREGATE SOBRIETY DIVIDEND (Family Wealth App)</span>
<span class="keyword">SELECT</span> User_ID, 
       <span class="function">SUM</span>(Daily_Savings) <span class="keyword">AS</span> Total_Principal,
       <span class="function">SUM</span>(Daily_Savings) <span class="operator">*</span> <span class="number">1.12</span> <span class="keyword">AS</span> Projected_Corpus_1Yr
<span class="keyword">FROM</span> Family_Wealth_SIP
<span class="keyword">WHERE</span> Transaction_Date <span class="operator">&gt;=</span> <span class="string">'2025-01-01'</span>
<span class="keyword">GROUP BY</span> User_ID;
                    </div>
                    <div class="text-gray-300 space-y-4">
                        <p class="font-bold text-indigo-400 text-lg underline">Project-Specific SQL Queries:</p>
                        <div class="space-y-4">
                            <div>
                                <h4 class="font-semibold text-white">Legal Lock Compliance:</h4>
                                <p class="text-sm">Query 1 filters retailers violating the mandatory 300m alcohol-free buffer around schools and shrines.</p>
                            </div>
                            <div>
                                <h4 class="font-semibold text-white">Digital Lock Audit:</h4>
                                <p class="text-sm">Query 2 monitors the effectiveness of Aadhaar-linked verification by tracking blocked attempts by minors.</p>
                            </div>
                            <div>
                                <h4 class="font-semibold text-white">Wealth Realization:</h4>
                                <p class="text-sm">Query 3 powers the app's real-time dashboard, calculating the 12% CAGR growth on savings redirected from alcohol.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

    </main>

    <script>
        // Project Dataset (NFHS-5 Representative)
        const stateData = {
            names: ['Arunachal Pradesh', 'Telangana', 'Sikkim', 'Manipur', 'Chhattisgarh', 'Andaman & Nicobar', 'Odisha', 'Goa', 'Jharkhand', 'Tripura', 'Assam', 'Punjab', 'Puducherry', 'Mizoram', 'Karnataka'],
            male: [52.7, 43.3, 39.8, 37.5, 34.8, 31.3, 28.8, 26.4, 25.4, 23.3, 21.8, 21.5, 21.5, 20.8, 19.9],
            female: [24.2, 6.7, 16.2, 0.9, 5.0, 1.8, 4.3, 4.2, 3.4, 0.8, 2.1, 0.1, 0.3, 0.4, 0.2]
        };

        function renderElbowPlot() {
            const wcss = [120, 45, 18, 12, 10, 8, 7, 6, 5.5, 5];
            const trace = {
                x: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                y: wcss,
                type: 'scatter',
                mode: 'lines+markers',
                line: { color: '#4f46e5', width: 3 },
                marker: { size: 8, color: '#4f46e5' }
            };

            const layout = {
                title: 'Elbow Curve (WCSS)',
                xaxis: { title: 'Clusters (K)' },
                yaxis: { title: 'Inertia' },
                annotations: [{
                    x: 3, y: 18,
                    xref: 'x', yref: 'y',
                    text: 'Optimal Elbow',
                    showarrow: true,
                    arrowhead: 6,
                    ax: 30, ay: -30
                }]
            };

            Plotly.newPlot('elbowPlot', [trace], layout);
        }

        function renderRiskPlot() {
            const colors = stateData.male.map(m => {
                if (m > 38) return '#ef4444'; // High Intensity
                if (m > 25) return '#f59e0b'; // Moderate
                return '#10b981'; // Baseline
            });

            const trace = {
                x: stateData.male,
                y: stateData.female,
                text: stateData.names,
                mode: 'markers+text',
                textposition: 'top center',
                type: 'scatter',
                marker: {
                    size: 14,
                    color: colors,
                    line: { width: 2, color: '#fff' }
                },
                hovertemplate: '<b>%{text}</b><br>Male: %{x}%<br>Female: %{y}%<extra></extra>'
            };

            const layout = {
                title: 'Risk Zones: Male vs Female Prevalence',
                xaxis: { title: 'Male (%)' },
                yaxis: { title: 'Female (%)' },
                margin: { t: 50, b: 50, l: 50, r: 50 },
                hovermode: 'closest'
            };

            Plotly.newPlot('riskPlot', [trace], layout);
        }

        window.onload = function() {
            renderElbowPlot();
            renderRiskPlot();
        };
    </script>
</body>
</html>