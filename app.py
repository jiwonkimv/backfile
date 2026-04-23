import streamlit as st

st.set_page_config(
    page_title="Jiwon Kim — Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,800;1,700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"], .stApp { font-family: 'Plus Jakarta Sans', sans-serif; background: #FDFCFA !important; color: #1a1a2e; }
.main { background: #FDFCFA !important; }
.main > div { padding: 0 !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display: none; }
[data-testid="stHeader"] { display: none; }

.hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 40%, #f093fb 100%);
    padding: 80px 8% 90px; position: relative; overflow: hidden;
}
.hero::before {
    content: ''; position: absolute; inset: 0;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
.hero::after {
    content: ''; position: absolute; bottom: -2px; left: 0; right: 0;
    height: 60px; background: #FDFCFA;
    clip-path: ellipse(55% 100% at 50% 100%);
}
.hero-tag {
    display: inline-block; background: rgba(255,255,255,0.2); backdrop-filter: blur(10px);
    color: white; font-size: 11px; font-weight: 600; letter-spacing: 3px;
    text-transform: uppercase; padding: 6px 16px; border-radius: 100px;
    margin-bottom: 24px; border: 1px solid rgba(255,255,255,0.3);
}
.hero-name {
    font-family: 'Playfair Display', serif; font-size: clamp(52px, 7vw, 88px);
    font-weight: 800; color: white; line-height: 1.05; letter-spacing: -2px;
    margin-bottom: 12px; text-shadow: 0 2px 20px rgba(0,0,0,0.15);
}
.hero-name span { font-style: italic; font-weight: 700; }
.hero-subtitle { font-size: 17px; font-weight: 400; color: rgba(255,255,255,0.85); margin-bottom: 32px; }
.hero-links { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 48px; }
.hero-link {
    display: inline-flex; align-items: center; gap: 6px;
    background: rgba(255,255,255,0.15); backdrop-filter: blur(10px);
    color: white !important; text-decoration: none !important;
    font-size: 12px; font-weight: 500; padding: 8px 16px; border-radius: 100px;
    border: 1px solid rgba(255,255,255,0.25);
}
.hero-stats-row {
    display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;
    position: relative; z-index: 1;
}
.hero-stat {
    background: rgba(255,255,255,0.15); backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.25); border-radius: 16px;
    padding: 20px 24px; text-align: center;
}
.hero-stat-n { font-family: 'Playfair Display', serif; font-size: 36px; font-weight: 800; color: white; line-height: 1; }
.hero-stat-l { font-size: 11px; color: rgba(255,255,255,0.7); margin-top: 6px; }

div[data-baseweb="tab-list"] {
    background: white !important; border-bottom: 2px solid #f0f0f0 !important;
    padding: 0 8% !important; gap: 0 !important;
    box-shadow: 0 2px 20px rgba(0,0,0,0.06) !important;
}
div[data-baseweb="tab"] {
    font-family: 'Space Grotesk', sans-serif !important; font-size: 13px !important;
    font-weight: 600 !important; color: #888 !important; letter-spacing: 0.5px !important;
    padding: 16px 24px !important; border-bottom: 2px solid transparent !important;
}
div[aria-selected="true"] { color: #667eea !important; border-bottom-color: #667eea !important; }

.section { padding: 60px 8%; }
.section-white { background: white; }
.section-tint  { background: #F7F5FF; }

.label {
    display: inline-flex; align-items: center; gap: 8px;
    font-size: 10px; font-weight: 700; letter-spacing: 3px;
    text-transform: uppercase; color: #667eea; margin-bottom: 8px;
}
.label::before { content: ''; width: 20px; height: 2px; background: linear-gradient(90deg, #667eea, #f093fb); border-radius: 1px; }
.sec-title { font-family: 'Playfair Display', serif; font-size: clamp(28px, 4vw, 42px); font-weight: 800; color: #1a1a2e; letter-spacing: -1px; line-height: 1.15; margin-bottom: 8px; }
.sec-sub { font-size: 15px; color: #666; font-weight: 400; margin-bottom: 40px; max-width: 600px; line-height: 1.7; }

.profile-body { font-size: 15px; line-height: 1.9; color: #444; max-width: 780px; }
.profile-body strong { color: #1a1a2e; font-weight: 600; }

.highlight-card { border-radius: 20px; padding: 28px 32px; }
.hc-purple { background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%); border: 1.5px solid #667eea30; }
.hc-orange { background: #FFF3E0; border: 1.5px solid #FFB74D50; }
.hc-green  { background: #E8F5E9; border: 1.5px solid #66BB6A50; }
.hc-num { font-family: 'Playfair Display', serif; font-size: 44px; font-weight: 800; background: linear-gradient(135deg, #667eea, #f093fb); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; line-height: 1; margin-bottom: 4px; }
.hc-num-o { font-family: 'Playfair Display', serif; font-size: 44px; font-weight: 800; color: #F57C00; line-height: 1; margin-bottom: 4px; }
.hc-num-g { font-family: 'Playfair Display', serif; font-size: 44px; font-weight: 800; color: #388E3C; line-height: 1; margin-bottom: 4px; }
.hc-label { font-size: 13px; color: #555; font-weight: 500; line-height: 1.5; }

.timeline { position: relative; padding-left: 24px; }
.timeline::before { content: ''; position: absolute; left: 0; top: 8px; bottom: 8px; width: 2px; background: linear-gradient(180deg, #667eea 0%, #f093fb 50%, #ffd700 100%); border-radius: 1px; }
.tl-card { background: white; border-radius: 20px; padding: 28px 32px; margin-bottom: 20px; box-shadow: 0 4px 24px rgba(102,126,234,0.08); border: 1.5px solid #f0f0f8; position: relative; }
.tl-card::before { content: ''; position: absolute; left: -32px; top: 28px; width: 16px; height: 16px; border-radius: 50%; background: linear-gradient(135deg, #667eea, #764ba2); border: 3px solid white; box-shadow: 0 0 0 2px #667eea40; }
.tl-role { font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; color: #1a1a2e; margin-bottom: 2px; }
.tl-company { font-size: 13px; font-weight: 700; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; letter-spacing: 0.5px; margin-bottom: 4px; }
.tl-period { font-family: 'Space Grotesk', sans-serif; font-size: 11px; color: #aaa; letter-spacing: 1px; font-weight: 500; margin-bottom: 14px; }
.tl-portfolio { background: linear-gradient(135deg, #667eea08, #f093fb08); border: 1px solid #667eea20; border-radius: 10px; padding: 10px 16px; font-size: 12px; color: #555; font-family: 'Space Grotesk', sans-serif; font-weight: 500; margin-bottom: 18px; }
.sub-head { font-size: 10px; font-weight: 700; letter-spacing: 2.5px; text-transform: uppercase; color: #667eea; margin: 20px 0 10px; display: flex; align-items: center; gap: 8px; }
.sub-head::after { content: ''; flex: 1; height: 1px; background: #667eea20; }
.bul { font-size: 13.5px; color: #444; line-height: 1.75; padding-left: 18px; position: relative; margin-bottom: 10px; }
.bul::before { content: '▸'; position: absolute; left: 0; background: linear-gradient(135deg, #667eea, #f093fb); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 10px; top: 4px; }
.bul b { color: #1a1a2e; font-weight: 600; }
.kpis { display: flex; flex-wrap: wrap; gap: 8px; margin: 8px 0 4px; }
.kpi        { background: linear-gradient(135deg, #667eea15, #764ba215); border: 1px solid #667eea30; border-radius: 100px; padding: 4px 14px; font-size: 11px; font-weight: 700; color: #5a67d8; font-family: 'Space Grotesk', sans-serif; }
.kpi-orange { background: #FFF3E0; border: 1px solid #FFB74D60; border-radius: 100px; padding: 4px 14px; font-size: 11px; font-weight: 700; color: #E65100; font-family: 'Space Grotesk', sans-serif; }
.kpi-green  { background: #E8F5E9; border: 1px solid #66BB6A60; border-radius: 100px; padding: 4px 14px; font-size: 11px; font-weight: 700; color: #2E7D32; font-family: 'Space Grotesk', sans-serif; }

.proj-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
.proj-card { border-radius: 20px; padding: 28px 30px; position: relative; overflow: hidden; }
.proj-p { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.proj-o { background: linear-gradient(135deg, #f7971e 0%, #ffd200 100%); }
.proj-b { background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); }
.proj-r { background: linear-gradient(135deg, #f953c6 0%, #b91d73 100%); }
.proj-card::after { content: ''; position: absolute; top: -40px; right: -40px; width: 120px; height: 120px; border-radius: 50%; background: rgba(255,255,255,0.1); }
.proj-num { font-family: 'Playfair Display', serif; font-size: 11px; font-weight: 700; color: rgba(255,255,255,0.6); letter-spacing: 2px; text-transform: uppercase; margin-bottom: 12px; }
.proj-title { font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 700; color: white; line-height: 1.3; margin-bottom: 8px; }
.proj-meta { font-size: 11px; color: rgba(255,255,255,0.7); margin-bottom: 16px; font-weight: 500; }
.proj-kpis { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 16px; }
.proj-kpi { background: rgba(255,255,255,0.2); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.3); border-radius: 100px; padding: 3px 12px; font-size: 11px; font-weight: 700; color: white; font-family: 'Space Grotesk', sans-serif; }
.proj-bul { font-size: 13px; color: rgba(255,255,255,0.9); line-height: 1.7; padding-left: 16px; position: relative; margin-bottom: 8px; }
.proj-bul::before { content: '→'; position: absolute; left: 0; color: rgba(255,255,255,0.5); font-size: 11px; top: 2px; }
.proj-bul b { color: white; }

.skill-cat { background: white; border-radius: 16px; padding: 24px 28px; margin-bottom: 16px; border: 1.5px solid #f0f0f8; box-shadow: 0 2px 16px rgba(102,126,234,0.06); }
.skill-cat-title { font-size: 11px; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: #667eea; margin-bottom: 14px; display: flex; align-items: center; gap: 8px; }
.skill-cat-title::before { content: ''; width: 6px; height: 6px; border-radius: 50%; background: linear-gradient(135deg, #667eea, #f093fb); }
.skill-tags { display: flex; flex-wrap: wrap; gap: 8px; }
.skill-tag { background: #F7F5FF; border: 1px solid #667eea25; border-radius: 8px; padding: 7px 14px; font-size: 12px; font-weight: 500; color: #444; }

.edu-card { background: white; border-radius: 20px; padding: 28px 32px; margin-bottom: 16px; border: 1.5px solid #f0f0f8; box-shadow: 0 2px 16px rgba(0,0,0,0.05); display: flex; align-items: flex-start; gap: 20px; }
.edu-icon { width: 48px; height: 48px; border-radius: 12px; flex-shrink: 0; background: linear-gradient(135deg, #667eea, #764ba2); display: flex; align-items: center; justify-content: center; font-size: 22px; }
.edu-degree { font-family: 'Playfair Display', serif; font-size: 18px; font-weight: 700; color: #1a1a2e; margin-bottom: 2px; }
.edu-school { font-size: 13px; font-weight: 600; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 4px; }
.edu-period { font-size: 11px; color: #aaa; font-family: 'Space Grotesk', sans-serif; letter-spacing: 1px; margin-bottom: 10px; }

.footer { background: linear-gradient(135deg, #667eea, #764ba2); padding: 48px 8%; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; }
.footer-name { font-family: 'Playfair Display', serif; font-size: 24px; font-weight: 800; color: white; }
.footer-contact { font-size: 13px; color: rgba(255,255,255,0.8); margin-top: 4px; }
.footer-links { display: flex; gap: 16px; }
.footer-link { font-size: 12px; font-weight: 600; color: rgba(255,255,255,0.7); text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.3); padding-bottom: 1px; }
</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div style="position:relative;z-index:1">
    <div class="hero-tag">✦ Retail Merchandising · Brand Activation · South Korea</div>
    <div class="hero-name">Jiwon <span>Kim</span></div>
    <div class="hero-subtitle">Turning retail spaces into brand experiences that convert &amp; stay memorable</div>
    <div class="hero-links">
      <a class="hero-link" href="tel:+821026573623">📞 (+82) 10-2657-3623</a>
      <a class="hero-link" href="mailto:jiwonkimv@gmail.com">✉️ jiwonkimv@gmail.com</a>
      <a class="hero-link" href="https://linkedin.com/in/jiwon-kim-673244226" target="_blank">🔗 LinkedIn</a>
    </div>
    <div class="hero-stats-row">
      <div class="hero-stat"><div class="hero-stat-n">5+</div><div class="hero-stat-l">Years in Retail</div></div>
      <div class="hero-stat"><div class="hero-stat-n">$350M+</div><div class="hero-stat-l">Total GMV Managed</div></div>
      <div class="hero-stat"><div class="hero-stat-n">50+</div><div class="hero-stat-l">Brand Partners</div></div>
      <div class="hero-stat"><div class="hero-stat-n">37</div><div class="hero-stat-l">Retail Locations</div></div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── TABS ──────────────────────────────────────────────────────────────────────
t_profile, t_exp, t_projects, t_skills, t_edu = st.tabs([
    "✦  Profile", "💼  Experience", "🚀  Key Projects", "⚡  Skills", "🎓  Education"
])

# ── PROFILE ───────────────────────────────────────────────────────────────────
with t_profile:
    st.markdown('<div class="section section-white">', unsafe_allow_html=True)
    st.markdown('<div class="label">About</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Retail Meets<br>Physical Experience</div>', unsafe_allow_html=True)
    st.markdown("""
    <p class="profile-body">
      Retail merchandising and brand activation professional with <strong>5+ years</strong> managing
      multi-brand programs across <strong>50+ locations</strong> in Korea's CE and lifestyle retail landscape.<br><br>
      Proven in executing pop-up and in-store display programs, managing vendor and agency relationships,
      and driving measurable sell-through results. Deep familiarity with the South Korean CE retail
      environment — including <strong>Lotte Hi-mart</strong>, department store shop-in-shop formats,
      and omni-channel activations.<br><br>
      Passionate about bringing emerging technology products to life in-store through compelling physical experiences.
    </p>
    """, unsafe_allow_html=True)
    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""<div class="highlight-card hc-purple">
          <div class="hc-num">$4M</div>
          <div class="hc-label">Single campaign GMV<br><span style="color:#888;font-size:12px">111% of target · +12.1% YoY</span></div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="highlight-card hc-orange">
          <div class="hc-num-o">+30%</div>
          <div class="hc-label">Daily views at Naver<br><span style="color:#888;font-size:12px">Data-driven content curation</span></div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="highlight-card hc-green">
          <div class="hc-num-g">+23%</div>
          <div class="hc-label">Rental increase closed<br><span style="color:#888;font-size:12px">5-year stalled Hi-mart negotiation</span></div>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── EXPERIENCE ────────────────────────────────────────────────────────────────
with t_exp:
    st.markdown('<div class="section section-tint">', unsafe_allow_html=True)
    st.markdown('<div class="label">Career</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Experience</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">5+ years across department store HQ buying, pop-up execution, and CE retail operations.</div>', unsafe_allow_html=True)
    st.markdown('<div class="timeline">', unsafe_allow_html=True)

    st.markdown("""
    <div class="tl-card">
      <div class="tl-role">Buyer, Consumer Electronics (GL)</div>
      <div class="tl-company">Lotte Department Store HQ</div>
      <div class="tl-period">AUG 2025 – PRESENT</div>
      <div class="tl-portfolio">📊 $190M+ annual GMV · 37 locations · 50+ brands · Lotte Hi-mart partner (450+ stores nationwide)</div>
      <div class="sub-head">Retail Display Program Management</div>
      <div class="bul">Planned and executed <b>built-in kitchen pop-up (Baekjo Sink)</b> — led full lifecycle from brand sourcing through in-store installation over 5 months
        <div class="kpis"><span class="kpi">$130K GMV</span><span class="kpi">$40K online + $90K in-store</span><span class="kpi">Busan relay May 2026</span></div>
      </div>
      <div class="bul">Managed <b>Lunar New Year Health Appliance Campaign</b> across 9 brands simultaneously
        <div class="kpis"><span class="kpi">$4M GMV</span><span class="kpi">111.4% of target</span><span class="kpi">+12.1% YoY</span></div>
      </div>
      <div class="bul">Executed <b>Zespa influencer-linked product launch</b> — display, demo, and creator content in tandem
        <div class="kpis"><span class="kpi">$157K revenue</span><span class="kpi">70 units sold out</span><span class="kpi">Margin +2%p</span></div>
      </div>
      <div class="sub-head">Lotte Hi-mart Partnership & CE Retail Operations</div>
      <div class="bul">Primary commercial liaison to <b>Lotte Hi-mart (450+ stores)</b> — lease terms, display space negotiations, execution standards</div>
      <div class="bul">Closed a <b>5-year stalled lease negotiation at +23% rental increase</b> — largest Hi-mart renewal nationally</div>
      <div class="bul">Drove <b>+11.6% YoY revenue growth (2026)</b> through vendor mix optimization and new brand programs</div>
      <div class="sub-head">Vendor & Agency Coordination</div>
      <div class="bul">Led annual JBP sessions with <b>50+ strategic brand partners</b> — promotional calendars, display investment, KPI tracking</div>
      <div class="bul">Coordinated cross-functional teams (marketing, creative, ops, logistics) to deliver concurrent programs on time and on budget</div>
      <div class="bul">Managed dual-channel P&amp;L; tracked sell-through, ASP, and promotional ROI weekly via advanced Excel</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tl-card">
      <div class="tl-role">Buyer, Home & Living</div>
      <div class="tl-company">Lotte Outlet HQ</div>
      <div class="tl-period">JAN 2023 – JUL 2025</div>
      <div class="tl-portfolio">📊 $160M+ annual revenue · 21 locations · 134 brands (Furniture, Kitchenware, Home Décor, Appliances)</div>
      <div class="sub-head">High-Impact Brand Activation & Pop-Up</div>
      <div class="bul"><b>Asahi Super Dry pop-up</b> — Korea's first retail activation of its kind; 13 press features, zero paid media spend; became internal company benchmark
        <div class="kpis"><span class="kpi-orange">$120K revenue</span><span class="kpi-orange">6,000 transactions</span><span class="kpi-orange">1,300+ new customers</span><span class="kpi-orange">14 days</span></div>
      </div>
      <div class="bul">Recruited and launched <b>Kim Gane Super pop-up</b> (channel-first in Korean dept store/outlet) — business case from scratch, installation, experience design</div>
      <div class="bul">Led <b>Dongdaemun district renewal</b>: recruited 2 new tenants (Daiso, Whose Fan Café) using foreign visitor traffic data; managed full onboarding for both brands</div>
      <div class="sub-head">Category Strategy & Performance</div>
      <div class="bul">Maintained <b>+6.3% YoY growth</b> across full portfolio (21 locations, 134 brands)</div>
      <div class="bul">Identified underperforming Samsung shop-in-shop, led tenant replacement — converted <b>negative contribution to positive operating profit</b></div>
      <div class="bul">Increased category commission by <b>+2–3%p</b> through margin code restructuring across 134 brands</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tl-card">
      <div class="tl-role">Store Operations (Part Leader)</div>
      <div class="tl-company">Lotte Department Store — Dongtan Branch</div>
      <div class="tl-period">FEB 2022 – DEC 2022</div>
      <div class="bul">Managed in-store vendor performance across CE, Furniture, and Kitchen categories — display compliance, tenant management, real-time execution response</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="label" style="margin-top:40px;margin-bottom:16px">Early Career</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="tl-card">
      <div class="tl-role">Content & Data Strategy Intern</div>
      <div class="tl-company">Naver — Korea's largest search & content platform</div>
      <div class="tl-period">JAN – APR 2021</div>
      <div class="bul">Managed content curation for <b>Naver Eohakdang</b> — diagnosed low engagement (&lt;1 daily view/user); analyzed 6 months of data; identified preference for article-format &amp; spoken English with peak CTR at commute hours</div>
      <div class="bul">Executed 3 data-driven interventions: rebalanced content mix (60% video → 60% article), produced original slang series, surfaced quiz at commute-hour top slot (1.5× higher CTR)
        <div class="kpis"><span class="kpi-green">+30% daily views</span><span class="kpi-green">Within 3 months</span></div>
      </div>
    </div>
    <div class="tl-card">
      <div class="tl-role">Marketing & Content Strategy Intern</div>
      <div class="tl-company">Colley — IP licensing & commerce platform</div>
      <div class="tl-period">MAY – AUG 2021</div>
      <div class="bul">Increased user retention by <b>40%</b> through personalized push notification strategy; experience in IP licensing and brand partnership environments</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

# ── KEY PROJECTS ──────────────────────────────────────────────────────────────
with t_projects:
    st.markdown('<div class="section section-white">', unsafe_allow_html=True)
    st.markdown('<div class="label">Highlights</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Key Projects</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-sub">Selected initiatives showcasing end-to-end ownership, creative execution, and measurable results.</div>', unsafe_allow_html=True)
    st.markdown('<div class="proj-grid">', unsafe_allow_html=True)

    st.markdown("""
    <div class="proj-card proj-p">
      <div class="proj-num">Project 01</div>
      <div class="proj-title">Built-in Kitchen Zone — Jamsil</div>
      <div class="proj-meta">Opening May 2026 · Gaggenau · Liebherr · Fhiaba · 9-month program</div>
      <div class="proj-kpis"><span class="proj-kpi">3 Global Brands</span><span class="proj-kpi">Sep 2024 → May 2026</span><span class="proj-kpi">End-to-End Ownership</span></div>
      <div class="proj-bul">Led full lifecycle of Korea's first premium multi-brand built-in kitchen zone — initial planning through construction and coordinated opening</div>
      <div class="proj-bul"><b>Primary liaison</b> between brand partners, design teams, and construction vendors — resolved global logo/fixture vs. store standard conflicts</div>
      <div class="proj-bul">Reviewed &amp; approved interior proposals across 3 brands, aligning spatial layout and tone-and-manner</div>
      <div class="proj-bul">Designed <b>repeat-visit engagement programs</b> (cooking classes, private events) to convert high-consideration shoppers</div>
    </div>
    <div class="proj-card proj-o">
      <div class="proj-num">Project 02</div>
      <div class="proj-title">Asahi Super Dry Draft Beer Can Pop-up</div>
      <div class="proj-meta">Korea's first retail activation of this kind · 14 days · Zero paid media</div>
      <div class="proj-kpis"><span class="proj-kpi">$120K Revenue</span><span class="proj-kpi">6,000 Transactions</span><span class="proj-kpi">1,300+ New Customers</span><span class="proj-kpi">13 Press Features</span></div>
      <div class="proj-bul">Conceived and executed from scratch — product sampling, storytelling, and interactive engagement environment</div>
      <div class="proj-bul">Managed vendor coordination, display setup, and in-store execution end-to-end</div>
      <div class="proj-bul"><b>Became internal company benchmark</b> for brand activation; 46% of customers aged 25–35</div>
    </div>
    <div class="proj-card proj-b">
      <div class="proj-num">Project 03</div>
      <div class="proj-title">Lunar New Year Health Appliance Campaign</div>
      <div class="proj-meta">9 brands simultaneously · Multi-channel · In-store + Online</div>
      <div class="proj-kpis"><span class="proj-kpi">$4M GMV</span><span class="proj-kpi">111.4% of Target</span><span class="proj-kpi">+12.1% YoY</span></div>
      <div class="proj-bul">Managed end-to-end execution across 9 brands simultaneously — coordinated display, pop-up activations, and online promotions in parallel</div>
      <div class="proj-bul">Built cross-functional project trackers; maintained execution documentation across all 9 brand initiatives</div>
    </div>
    <div class="proj-card proj-r">
      <div class="proj-num">Project 04</div>
      <div class="proj-title">Naver Eohakdang Content Strategy</div>
      <div class="proj-meta">Data-driven content curation · 3-month sprint</div>
      <div class="proj-kpis"><span class="proj-kpi">+30% Daily Views</span><span class="proj-kpi">1.5× CTR Boost</span><span class="proj-kpi">3 Interventions</span></div>
      <div class="proj-bul">Diagnosed engagement problem (&lt;1 daily view/user) via 6-month data analysis — format + timing insights</div>
      <div class="proj-bul">Rebalanced content mix; produced spoken-English series; placed quiz at commute-hour top slot</div>
      <div class="proj-bul"><b>+30% daily view increase</b> within 3 months</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

# ── SKILLS ────────────────────────────────────────────────────────────────────
with t_skills:
    st.markdown('<div class="section section-tint">', unsafe_allow_html=True)
    st.markdown('<div class="label">Capabilities</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Core Competencies</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        for cat, skills in [
            ("Activation & Display", ["Pop-Up & Display Program Management", "In-Store Execution & Compliance", "Visual Merchandising Strategy", "Retail Layout & Flow Optimization", "Customer Engagement Design"]),
            ("Operations & Tools", ["Project Tracking & Reporting", "Advanced Excel (Pivot, Scenario Analysis)", "AI Tools Integration", "Omni-Channel Activation", "Dual-Channel P&L Management"]),
        ]:
            tags = "".join(f'<span class="skill-tag">{s}</span>' for s in skills)
            st.markdown(f'<div class="skill-cat"><div class="skill-cat-title">{cat}</div><div class="skill-tags">{tags}</div></div>', unsafe_allow_html=True)
    with col2:
        for cat, skills in [
            ("Commercial & Strategy", ["CE Retail Partner Management", "Budget & P&L Management", "Sell-Through & KPI Analysis", "Promotional ROI Tracking", "New Brand / Merchant Sourcing"]),
            ("Stakeholder Management", ["Vendor & Agency Coordination", "Cross-Functional Collaboration", "Consumer Insights & Analytics", "Lotte Hi-mart / CE Channel", "JBP & Partner Negotiation"]),
        ]:
            tags = "".join(f'<span class="skill-tag">{s}</span>' for s in skills)
            st.markdown(f'<div class="skill-cat"><div class="skill-cat-title">{cat}</div><div class="skill-tags">{tags}</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ── EDUCATION ─────────────────────────────────────────────────────────────────
with t_edu:
    st.markdown('<div class="section section-white">', unsafe_allow_html=True)
    st.markdown('<div class="label">Academic</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Education</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="edu-card">
      <div class="edu-icon">🎓</div>
      <div>
        <div class="edu-degree">B.A. in Russian Studies</div>
        <div class="edu-school">Chung-Ang University</div>
        <div class="edu-period">MAR 2017 – AUG 2021</div>
        <div class="bul">Marketing, Corporate Finance, Managerial Accounting, Consumer Behavior, Organizational Behavior, International Business</div>
      </div>
    </div>
    <div class="edu-card">
      <div class="edu-icon">✈️</div>
      <div>
        <div class="edu-degree">Exchange Student</div>
        <div class="edu-school">Higher School of Economics (HSE), St. Petersburg, Russia</div>
        <div class="edu-period">EXCHANGE SEMESTER</div>
        <div class="bul">International academic experience at one of Russia's top research universities</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <div>
    <div class="footer-name">Jiwon Kim</div>
    <div class="footer-contact">Retail Merchandising &amp; Brand Activation · South Korea</div>
  </div>
  <div class="footer-links">
    <a class="footer-link" href="mailto:jiwonkimv@gmail.com">jiwonkimv@gmail.com</a>
    <a class="footer-link" href="tel:+821026573623">(+82) 10-2657-3623</a>
    <a class="footer-link" href="https://linkedin.com/in/jiwon-kim-673244226">LinkedIn</a>
  </div>
</div>
""", unsafe_allow_html=True)
