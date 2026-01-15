from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>LearnQuest</title>

<style>
*{
    box-sizing:border-box;
    font-family: "Segoe UI", system-ui, sans-serif;
}

body{
    margin:0;
    background:#f7f9fc;
    color:#1f2937;
}

/* ================= NAVBAR ================= */
.navbar{
    background:#ffffff;
    height:64px;
    display:flex;
    align-items:center;
    padding:0 28px;
    box-shadow:0 1px 6px rgba(0,0,0,0.08);
}

.logo{
    font-weight:700;
    color:#6366f1;
    font-size:20px;
    margin-right:40px;
}

.nav-links{
    display:flex;
    gap:24px;
    font-size:14px;
    color:#374151;
}

.nav-links span{
    cursor:pointer;
}

.nav-right{
    margin-left:auto;
    display:flex;
    align-items:center;
    gap:16px;
    font-size:14px;
}

.join-btn{
    background:#6366f1;
    color:white;
    border:none;
    padding:8px 14px;
    border-radius:8px;
}

/* ================= PAGE ================= */
.page{
    padding:32px;
}

.page h2{
    margin-bottom:4px;
}

.subtitle{
    color:#6b7280;
    font-size:14px;
    margin-bottom:24px;
}

/* ================= SUBJECT CARDS ================= */
.grid{
    display:grid;
    grid-template-columns:repeat(auto-fill,minmax(260px,1fr));
    gap:20px;
}

.card{
    background:white;
    padding:20px;
    border-radius:16px;
    box-shadow:0 6px 16px rgba(0,0,0,0.06);
    transition:0.2s;
}

.card:hover{
    transform:translateY(-3px);
}

.icon{
    width:36px;
    height:36px;
    border-radius:10px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:bold;
    margin-bottom:12px;
}

.math{background:#eef2ff;color:#4f46e5;}
.physics{background:#fdf4ff;color:#a855f7;}
.cs{background:#ecfeff;color:#0891b2;}
.bio{background:#ecfdf5;color:#059669;}
.history{background:#fff7ed;color:#ea580c;}

.card h4{
    margin:6px 0;
}

.desc{
    font-size:13px;
    color:#6b7280;
    margin-bottom:12px;
}

.progress{
    height:8px;
    background:#e5e7eb;
    border-radius:10px;
    overflow:hidden;
    margin-bottom:6px;
}

.bar{
    height:8px;
    background:#6366f1;
}

.meta{
    font-size:12px;
    color:#6b7280;
}

/* ================= RESPONSIVE ================= */
@media(max-width:700px){
    .nav-links{display:none;}
    .page{padding:20px;}
}
</style>

</head>
<body>

<!-- NAVBAR -->
<div class="navbar">
    <div class="logo">LearnQuest</div>

    <div class="nav-links">
        <span>Dashboard</span>
        <span>Quiz</span>
        <span><b>Subjects</b></span>
        <span>Compete</span>
        <span>Achievements</span>
        <span>Progress</span>
        <span>Teacher</span>
    </div>

    <div class="nav-right">
        <span>Chanchal Gupta</span>
        <button class="join-btn">Join Class</button>
    </div>
</div>

<!-- PAGE -->
<div class="page">
    <h2>All Subjects</h2>
    <div class="subtitle">Choose a subject to start learning</div>

    <div class="grid">

        <div class="card">
            <div class="icon math">∑</div>
            <h4>Mathematics</h4>
            <div class="desc">Master numbers, algebra, geometry, and problem-solving skills.</div>
            <div class="progress"><div class="bar" style="width:60%"></div></div>
            <div class="meta">Mastery • 60%</div>
        </div>

        <div class="card">
            <div class="icon physics">⚛</div>
            <h4>Physics</h4>
            <div class="desc">Explore the laws of nature, motion, energy, and forces.</div>
            <div class="progress"><div class="bar" style="width:45%"></div></div>
            <div class="meta">Mastery • 45%</div>
        </div>

        <div class="card">
            <div class="icon cs">&lt;/&gt;</div>
            <h4>Computer Science</h4>
            <div class="desc">Learn programming, algorithms, and computational thinking.</div>
            <div class="progress"><div class="bar" style="width:30%"></div></div>
            <div class="meta">Mastery • 30%</div>
        </div>

        <div class="card">
            <div class="icon bio">🧬</div>
            <h4>Biology</h4>
            <div class="desc">Discover living organisms, cells, ecosystems, and life processes.</div>
            <div class="progress"><div class="bar" style="width:80%"></div></div>
            <div class="meta">Mastery • 80%</div>
        </div>

        <div class="card">
            <div class="icon history">⌛</div>
            <h4>History</h4>
            <div class="desc">Journey through time and understand civilizations and events.</div>
            <div class="progress"><div class="bar" style="width:55%"></div></div>
            <div class="meta">Mastery • 55%</div>
        </div>

    </div>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
