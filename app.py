import streamlit as st
import base64, os

st.set_page_config(
    page_title="Jiwon Kim — Portfolio",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── 사진 로드 ─────────────────────────────────────────────────
PHOTO_B64 = ""
for p in ["photo.jpg", os.path.join(os.path.dirname(__file__), "photo.jpg")]:
    if os.path.exists(p):
        with open(p, "rb") as f:
            PHOTO_B64 = base64.b64encode(f.read()).decode()
        break

PHOTO_HTML = (
    f'<img src="data:image/jpeg;base64,{PHOTO_B64}" class="hero-photo" />'
    if PHOTO_B64 else
    '<div class="hero-photo" style="display:flex;align-items:center;justify-content:center;background:#E8F0FE;color:#3B6FE8;font-size:36px;font-weight:800">JK</div>'
)

st.markdown(f"""
<style>
@import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/variable/pretendardvariable.css');

*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

html, body, [class*="css"], .stApp {{
    font-family: 'Pretendard Variable', 'Pretendard', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background: #FFFFFF !important;
    color: #111827;
}}

/* ── Streamlit 컨테이너 완전 평탄화 ── */
.main, .main > div,
.stMainBlockContainer,
div[data-testid="stMainBlockContainer"],
div[data-testid="block-container"],
.block-container {{
    padding: 0 !important;
    max-width: 100% !important;
    background: #FFFFFF !important;
}}
section[data-testid="stSidebar"] {{ display: none; }}
[data-testid="stDecoration"] {{ display: none; }}
[data-testid="stHeader"] {{
    background: rgba(255,255,255,0.92) !important;
    backdrop-filter: blur(8px);
    border-bottom: 1px solid #F0F0F0;
}}

/* ── HERO ── */
.hero {{
    background: #FFFFFF;
    padding: 64px 9% 56px;
    display: flex;
    align-items: center;
    gap: 52px;
    border-bottom: 1.5px solid #F3F4F6;
}}
.hero-photo {{
    width: 140px;
    height: 172px;
    object-fit: cover;
    object-position: top center;
    border-radius: 16px;
    flex-shrink: 0;
    box-shadow: 0 8px 32px rgba(59,111,232,0.13), 0 2px 8px rgba(0,0,0,0.07);
    border: 2.5px solid #E8F0FE;
}}
.hero-body {{ flex: 1; }}
.hero-eyebrow {{
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #3B6FE8;
    margin-bottom: 10px;
}}
.hero-name {{
    font-size: clamp(40px, 5.5vw, 64px);
    font-weight: 800;
    color: #111827;
    line-height: 1.08;
    letter-spacing: -1.5px;
    margin-bottom: 10px;
}}
.hero-title {{
    font-size: 15px;
    font-weight: 400;
    color: #6B7280;
    margin-bottom: 28px;
    line-height: 1.6;
    letter-spacing: -0.1px;
}}
.hero-contacts {{
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 36px;
}}
.hero-contact {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: #F8F9FB;
    border: 1.5px solid #E5E7EB;
    border-radius: 8px;
    padding: 7px 14px;
    font-size: 12.5px;
    font-weight: 500;
    color: #374151 !important;
    text-decoration: none !important;
    transition: border-color .15s, background .15s;
}}
.hero-contact:hover {{
    border-color: #3B6FE8;
    background: #EEF3FD;
    color: #3B6FE8 !important;
}}
.share-btn {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #3B6FE8;
    border: none;
    border-radius: 8px;
    padding: 8px 18px;
    font-size: 12.5px;
    font-weight: 700;
    color: #FFFFFF !important;
    text-decoration: none !important;
    letter-spacing: -0.1px;
    box-shadow: 0 2px 10px rgba(59,111,232,0.3);
    transition: background .15s, box-shadow .15s;
}}
.share-btn:hover {{
    background: #2B5DD4;
    box-shadow: 0 4px 16px rgba(59,111,232,0.4);
}}
.hero-stats {{
    display: flex;
    gap: 36px;
    flex-wrap: wrap;
    padding-top: 28px;
    border-top: 1.5px solid #F3F4F6;
}}
.stat-box {{ text-align: left; }}
.stat-num {{
    font-size: 28px;
    font-weight: 800;
    color: #111827;
    line-height: 1;
    letter-spacing: -0.5px;
}}
.stat-num span {{ color: #3B6FE8; }}
.stat-label {{
    font-size: 11px;
    color: #9CA3AF;
    margin-top: 4px;
    font-weight: 500;
    letter-spacing: 0.3px;
}}

/* ── 탭 — 어두운 네이비 배경으로 명확하게 ── */
div[data-baseweb="tab-list"] {{
    background: #111827 !important;
    border-bottom: none !important;
    padding: 0 9% !important;
    gap: 2px !important;
    box-shadow: 0 2px 16px rgba(0,0,0,0.12) !important;
    position: sticky !important;
    top: 0 !important;
    z-index: 200 !important;
}}
div[data-baseweb="tab"] {{
    font-family: 'Pretendard Variable','Pretendard',sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    color: rgba(255,255,255,0.45) !important;
    padding: 17px 22px !important;
    letter-spacing: -0.1px !important;
    border-bottom: 3px solid transparent !important;
    margin-bottom: 0 !important;
    transition: color .15s !important;
}}
div[aria-selected="true"] {{
    color: #FFFFFF !important;
    border-bottom: 3px solid #3B6FE8 !important;
    font-weight: 700 !important;
    background: rgba(59,111,232,0.12) !important;
}}
div[data-baseweb="tab"]:hover {{
    color: rgba(255,255,255,0.8) !important;
    background: rgba(255,255,255,0.05) !important;
}}

/* ── 섹션 ── */
.section {{
    padding: 60px 9% !important;
    width: 100%;
    background: #FFFFFF;
}}
.section-gray {{
    padding: 60px 9% !important;
    width: 100%;
    background: #F9FAFB;
}}

.sec-label {{
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #3B6FE8;
    margin-bottom: 6px;
}}
.sec-title {{
    font-size: clamp(22px, 3vw, 34px);
    font-weight: 800;
    color: #111827;
    letter-spacing: -0.8px;
    line-height: 1.2;
    margin-bottom: 6px;
}}
.sec-desc {{
    font-size: 14.5px;
    color: #6B7280;
    line-height: 1.75;
    max-width: 600px;
    margin-bottom: 36px;
    font-weight: 400;
}}

/* ── KPI 카드 ── */
.kpi-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-top: 36px;
}}
.kpi-card {{
    background: #FFFFFF;
    border: 1.5px solid #E5E7EB;
    border-radius: 14px;
    padding: 22px 22px 20px;
    border-top: 3px solid #3B6FE8;
    transition: box-shadow .2s;
}}
.kpi-card:hover {{ box-shadow: 0 4px 16px rgba(59,111,232,0.1); }}
.kpi-num {{
    font-size: 30px;
    font-weight: 800;
    color: #111827;
    line-height: 1;
    margin-bottom: 8px;
    letter-spacing: -0.5px;
}}
.kpi-num b {{ color: #3B6FE8; }}
.kpi-desc {{
    font-size: 12.5px;
    color: #6B7280;
    line-height: 1.55;
    font-weight: 500;
}}

/* ── 타임라인 ── */
.tl-wrap {{ position: relative; padding-left: 22px; }}
.tl-wrap::before {{
    content: '';
    position: absolute;
    left: 0; top: 16px; bottom: 16px;
    width: 2px;
    background: linear-gradient(180deg, #3B6FE8 0%, #E5E7EB 100%);
    border-radius: 1px;
}}
.tl-card {{
    background: #FFFFFF;
    border: 1.5px solid #E5E7EB;
    border-radius: 16px;
    padding: 28px 30px;
    margin-bottom: 14px;
    position: relative;
    transition: box-shadow .2s;
}}
.tl-card:hover {{ box-shadow: 0 4px 20px rgba(0,0,0,0.07); }}
.tl-card::before {{
    content: '';
    position: absolute;
    left: -29px; top: 26px;
    width: 14px; height: 14px;
    border-radius: 50%;
    background: #3B6FE8;
    border: 3px solid #F9FAFB;
    box-shadow: 0 0 0 1.5px #3B6FE8;
}}
.tl-role {{
    font-size: 16.5px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 2px;
    letter-spacing: -0.3px;
}}
.tl-company {{
    font-size: 13px;
    font-weight: 600;
    color: #3B6FE8;
    margin-bottom: 3px;
    letter-spacing: -0.1px;
}}
.tl-period {{
    font-size: 11px;
    font-weight: 500;
    color: #9CA3AF;
    letter-spacing: 0.5px;
    margin-bottom: 12px;
}}
.tl-scope {{
    font-size: 12px;
    color: #6B7280;
    background: #F9FAFB;
    border-radius: 8px;
    padding: 8px 14px;
    margin-bottom: 18px;
    font-weight: 500;
    line-height: 1.6;
    border: 1px solid #F3F4F6;
}}
.sub-label {{
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #3B6FE8;
    margin: 18px 0 9px;
    display: flex;
    align-items: center;
    gap: 8px;
}}
.sub-label::after {{
    content: '';
    flex: 1;
    height: 1px;
    background: #E5E7EB;
}}
.bul {{
    font-size: 13.5px;
    color: #374151;
    line-height: 1.75;
    padding-left: 16px;
    position: relative;
    margin-bottom: 8px;
}}
.bul::before {{
    content: '—';
    position: absolute;
    left: 0;
    color: #3B6FE8;
    font-size: 11px;
    font-weight: 700;
    top: 3px;
}}
.bul b {{ color: #111827; font-weight: 700; }}
.badges {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin: 8px 0 2px;
}}
.badge {{
    background: #EEF3FD;
    border: 1px solid #C7D9F9;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 700;
    color: #2B5DD4;
    letter-spacing: -0.1px;
}}

/* ── 프로젝트 카드 ── */
.proj-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
}}
.proj-card {{
    background: #111827;
    border-radius: 16px;
    padding: 28px 28px 26px;
    position: relative;
    overflow: hidden;
    border-top: 3px solid #3B6FE8;
}}
.proj-card::before {{
    content: '';
    position: absolute;
    top: -50px; right: -50px;
    width: 130px; height: 130px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(59,111,232,0.18) 0%, transparent 70%);
}}
.proj-no {{
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    color: rgba(255,255,255,0.25);
    text-transform: uppercase;
    margin-bottom: 10px;
}}
.proj-title {{
    font-size: 17px;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 1.3;
    margin-bottom: 5px;
    letter-spacing: -0.3px;
}}
.proj-sub {{
    font-size: 11.5px;
    color: rgba(255,255,255,0.38);
    margin-bottom: 14px;
    font-weight: 500;
}}
.proj-badges {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 16px;
}}
.proj-badge {{
    background: rgba(59,111,232,0.22);
    border: 1px solid rgba(59,111,232,0.4);
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: 700;
    color: #93C5FD;
    letter-spacing: -0.1px;
}}
.proj-bul {{
    font-size: 13px;
    color: rgba(255,255,255,0.65);
    line-height: 1.7;
    padding-left: 14px;
    position: relative;
    margin-bottom: 7px;
}}
.proj-bul::before {{
    content: '→';
    position: absolute;
    left: 0;
    color: #3B6FE8;
    font-size: 11px;
    top: 3px;
}}
.proj-bul b {{ color: #FFFFFF; }}

/* ── 스킬 ── */
.skill-block {{
    background: #FFFFFF;
    border: 1.5px solid #E5E7EB;
    border-radius: 14px;
    padding: 22px 24px;
    margin-bottom: 12px;
    transition: box-shadow .2s;
}}
.skill-block:hover {{ box-shadow: 0 2px 12px rgba(0,0,0,0.06); }}
.skill-cat-title {{
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #374151;
    margin-bottom: 13px;
    display: flex;
    align-items: center;
    gap: 8px;
}}
.skill-cat-title::before {{
    content: '';
    width: 4px; height: 14px;
    border-radius: 2px;
    background: #3B6FE8;
}}
.skill-tags {{ display: flex; flex-wrap: wrap; gap: 7px; }}
.skill-tag {{
    background: #F9FAFB;
    border: 1px solid #E5E7EB;
    border-radius: 6px;
    padding: 6px 12px;
    font-size: 12.5px;
    font-weight: 500;
    color: #374151;
}}

/* ── 학력 ── */
.edu-card {{
    background: #FFFFFF;
    border: 1.5px solid #E5E7EB;
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 12px;
    display: flex;
    align-items: flex-start;
    gap: 18px;
}}
.edu-icon {{
    width: 44px; height: 44px;
    border-radius: 10px;
    background: #111827;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
}}
.edu-degree {{
    font-size: 16px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 3px;
    letter-spacing: -0.2px;
}}
.edu-school {{
    font-size: 12.5px;
    font-weight: 600;
    color: #3B6FE8;
    margin-bottom: 4px;
}}
.edu-period {{
    font-size: 11px;
    color: #9CA3AF;
    letter-spacing: 0.5px;
    font-weight: 500;
    margin-bottom: 10px;
}}

/* ── 푸터 ── */
.footer {{
    background: #111827;
    padding: 40px 9%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
}}
.footer-name {{
    font-size: 17px;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: -0.3px;
}}
.footer-sub {{
    font-size: 12px;
    color: rgba(255,255,255,0.35);
    margin-top: 3px;
}}
.footer-links {{ display: flex; gap: 16px; align-items: center; flex-wrap: wrap; }}
.footer-link {{
    font-size: 12.5px;
    font-weight: 500;
    color: rgba(255,255,255,0.45);
    text-decoration: none;
    transition: color .15s;
}}
.footer-link:hover {{ color: rgba(255,255,255,0.85); }}

div[data-testid="stMarkdownContainer"] p {{ margin: 0; }}
</style>
""", unsafe_allow_html=True)

# ─── HERO ────────────────────────────────────────────────────
linkedin = "https://linkedin.com/in/jiwon-kim-673244226"

st.markdown(f"""
<div class="hero">
  {PHOTO_HTML}
  <div class="hero-body">
    <div class="hero-eyebrow">◈ Portfolio · South Korea</div>
    <div class="hero-name">Jiwon Kim</div>
    <div class="hero-title">
      Retail Buyer &amp; Brand Activator &nbsp;·&nbsp; Lotte Department Store HQ &nbsp;·&nbsp; $350M+ GMV Managed
    </div>
    <div class="hero-contacts">
      <a class="hero-contact" href="tel:+821026573623">📞 (+82) 10-2657-3623</a>
      <a class="hero-contact" href="mailto:jiwonkimv@gmail.com">✉ jiwonkimv@gmail.com</a>
      <a class="hero-contact" href="{linkedin}" target="_blank">in LinkedIn</a>
      <a class="share-btn" href="{linkedin}" target="_blank">🔗 Share Profile</a>
    </div>
    <div class="hero-stats">
      <div class="stat-box">
        <div class="stat-num">5<span>+</span></div>
        <div class="stat-label">Years Experience</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">$350M<span>+</span></div>
        <div class="stat-label">GMV Managed</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">160<span>+</span></div>
        <div class="stat-label">Brand Partners</div>
      </div>
      <div class="stat-box">
        <div class="stat-num">55<span>+</span></div>
        <div class="stat-label">Locations</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── TABS ─────────────────────────────────────────────────────
t_about, t_exp, t_projects, t_skills, t_edu = st.tabs([
    "About", "Experience", "Key Projects", "Skills", "Education"
])

# ─── ABOUT ────────────────────────────────────────────────────
with t_about:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Commercial Retail Buyer<br>with a Track Record of Results</div>', unsafe_allow_html=True)
    st.markdown("""
    <p style="font-size:15px;line-height:1.85;color:#374151;max-width:760px;">
      Commercial retail buyer with <strong style="color:#111827;font-weight:700">5+ years</strong>
      of P&amp;L ownership across department store and outlet channels.
      Managed a multi-category portfolio of
      <strong style="color:#111827;font-weight:700">₩460B+ ($350M+)</strong>
      spanning 55+ locations and 160+ brands.<br><br>
      Track record of vendor negotiation, margin restructuring, pop-up activation, and turning
      underperforming assets into profit contributors.
      Led high-impact traffic activations with national media reach —
      including <strong style="color:#111827;font-weight:700">Korea's first Asahi Super Dry retail activation</strong>
      ($120K in 14 days, 13 press features) and the
      <strong style="color:#111827;font-weight:700">first premium built-in kitchen zone</strong>
      in a Korean department store.<br><br>
      Experienced in Joint Business Planning, influencer-linked commerce, IP retail programs,
      and cross-functional collaboration across Marketing, Finance, and Supply Chain.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="kpi-grid">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""<div class="kpi-card">
          <div class="kpi-num"><b>$4M</b></div>
          <div class="kpi-desc">Single campaign GMV<br>111% of target · +12.1% YoY</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="kpi-card">
          <div class="kpi-num"><b>+23%</b></div>
          <div class="kpi-desc">Rental increase secured<br>5-year stalled Hi-mart deal</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""<div class="kpi-card">
          <div class="kpi-num"><b>13</b></div>
          <div class="kpi-desc">Press features earned<br>Zero paid media spend</div>
        </div>""", unsafe_allow_html=True)
    with c4:
        st.markdown("""<div class="kpi-card">
          <div class="kpi-num"><b>+30%</b></div>
          <div class="kpi-desc">Daily views at Naver<br>Data-driven curation</div>
        </div>""", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ─── EXPERIENCE ───────────────────────────────────────────────
with t_exp:
    st.markdown('<div class="section-gray">', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Career</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Experience</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-desc">5+ years of progressive ownership across department store HQ buying, pop-up execution, and CE retail operations.</div>', unsafe_allow_html=True)

    st.markdown('<div class="tl-wrap">', unsafe_allow_html=True)

    st.markdown("""
    <div class="tl-card">
      <div class="tl-role">Buyer, Consumer Electronics (GL)</div>
      <div class="tl-company">Lotte Department Store HQ</div>
      <div class="tl-period">AUG 2025 – PRESENT</div>
      <div class="tl-scope">$190M+ annual GMV &nbsp;·&nbsp; 37 locations &nbsp;·&nbsp; 50+ brands &nbsp;·&nbsp; Lotte Hi-mart partner (450+ stores)</div>

      <div class="sub-label">P&L Ownership & Category Strategy</div>
      <div class="bul">Full category P&L responsibility — revenue planning, margin structure, commission model, and vendor profitability across premium appliance, built-in kitchen, wellness, audio, and specialty segments</div>
      <div class="bul">Drove <b>+11.6% YoY revenue growth (2026)</b> through vendor mix optimization, pricing strategy adjustment, and new brand activation</div>

      <div class="sub-label">Vendor Negotiation & Commercial Terms</div>
      <div class="bul">Closed a <b>5-year stalled lease negotiation with Lotte Hi-mart at +23% rental increase</b> — largest Hi-mart renewal in the national network</div>
      <div class="bul">Renegotiated commission structures during vendor onboarding; rebalanced premium vs. mid-tier assortment via contribution margin analysis</div>

      <div class="sub-label">Activation & Influencer-Linked Commerce</div>
      <div class="bul">Lunar New Year Health Appliance Campaign — <b>9 brands simultaneously</b>, display + pop-up + online in parallel
        <div class="badges"><span class="badge">$4M GMV</span><span class="badge">111.4% of target</span><span class="badge">+12.1% YoY</span></div>
      </div>
      <div class="bul">Zespa exclusive massage chair launch — partnered with ReviewMachine (200K subs CE YouTuber) for influencer group buy
        <div class="badges"><span class="badge">$157K revenue</span><span class="badge">70 units sold out</span><span class="badge">Margin +2%p</span></div>
      </div>
      <div class="bul">Recruited Baekjo Sink (premium built-in kitchen) after 5 months sourcing — ran influencer group buy alongside in-store pop-up
        <div class="badges"><span class="badge">$130K GMV</span><span class="badge">$40K online + $90K in-store</span></div>
      </div>

      <div class="sub-label">Key Projects</div>
      <div class="bul"><b>Built-in Kitchen Zone (Jamsil, Opening May 2026)</b> — Gaggenau · Liebherr · Fhiaba. Led 9-month end-to-end program: served as primary liaison between global brands, design teams, and construction vendors; resolved fixture/logo spec conflicts; designed repeat-visit engagement programs (cooking classes, private events) to convert high-consideration shoppers</div>

      <div class="sub-label">Data & JBP</div>
      <div class="bul">Weekly sell-through, ASP, and contribution margin reviews; led annual JBP sessions with 50+ brand partners; built Excel financial models (Pivot, VLOOKUP, Scenario Analysis) — 5+ years advanced Excel</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tl-card">
      <div class="tl-role">Buyer, Home & Living</div>
      <div class="tl-company">Lotte Outlet HQ</div>
      <div class="tl-period">JAN 2023 – JUL 2025</div>
      <div class="tl-scope">$160M+ annual revenue &nbsp;·&nbsp; 21 locations &nbsp;·&nbsp; 134 brands (Furniture, Bedding, Kitchenware, Home Décor, Appliances)</div>

      <div class="sub-label">High-Impact Brand Activation</div>
      <div class="bul"><b>Asahi Super Dry Draft Beer Can pop-up</b> — Korea's first; proactively identified Asahi issue and secured exclusive rights; organic coverage by @busanunnie (355K followers); zero paid media; became internal company benchmark
        <div class="badges"><span class="badge">$120K revenue</span><span class="badge">6,000 txns</span><span class="badge">1,300+ new customers</span><span class="badge">13 press features</span><span class="badge">14 days</span></div>
      </div>
      <div class="bul">Recruited Kim Gane Super pop-up (channel-first in Korean dept store/outlet) — cult F&amp;B brand known for viral queues; built business case from scratch</div>
      <div class="bul">Dongdaemun district renewal — recruited <b>Daiso + Whose Fan Café</b> using foreign visitor traffic data
        <div class="badges"><span class="badge">₩26.7억 revenue</span><span class="badge">₩1.8억 profit</span><span class="badge">Daiso ₩25억 annual</span></div>
      </div>
      <div class="bul">Licensed IP retail programs as channel differentiators: Gaspard &amp; Lisa, Whosfan Café, Playmobil Hangul Day, Disney Fluffy Festival, Moomin, Shinkai Makoto Shop, Haribo Living — all featured in national media</div>

      <div class="sub-label">P&L & Portfolio Rebalancing</div>
      <div class="bul">Maintained <b>+6.3% YoY growth</b> across full portfolio (21 locations, 134 brands)</div>
      <div class="bul">Replaced underperforming Samsung Electronics shop-in-shop — converted <b>negative contribution to positive operating profit</b></div>
      <div class="bul">Increased category commission <b>+2–3%p</b> via margin code restructuring; +7% better terms with Daiso; normalized terms for Hyundai Livart; established management fee structure for Modern House</div>

      <div class="sub-label">Online Activation</div>
      <div class="bul">Recruited Roborak, Deskr, Jinus for online campaigns; resolved 4-month Deskr suspension through renegotiation
        <div class="badges"><span class="badge">Deskr ₩4.6억 annual</span><span class="badge">Jinus ₩1.7억 annual</span></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tl-card">
      <div class="tl-role">Store Operations (Part Leader)</div>
      <div class="tl-company">Lotte Department Store — Dongtan Branch</div>
      <div class="tl-period">FEB 2022 – DEC 2022</div>
      <div class="bul">On-site vendor performance management across CE, Furniture, and Kitchen — display compliance monitoring, tenant management, real-time execution response</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sec-label" style="margin-top:40px;margin-bottom:14px">Early Career</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="tl-card">
      <div class="tl-role">Content & Data Strategy Intern</div>
      <div class="tl-company">Naver Corp — Korea's largest search & content platform</div>
      <div class="tl-period">JAN – APR 2021</div>
      <div class="bul">Managed content curation for <b>Naver Eohakdang</b> — diagnosed low engagement (&lt;1 daily view/user) via 6-month data analysis; identified preference for article-format &amp; spoken English, peak CTR during commute hours</div>
      <div class="bul">3 data-driven interventions: rebalanced content mix (60% video → 60% article), produced slang &amp; abbreviation series, surfaced quiz at commute-hour top placement (CTR 1.5×)
        <div class="badges"><span class="badge">+30% daily views</span><span class="badge">3 months</span></div>
      </div>
    </div>
    <div class="tl-card">
      <div class="tl-role">Marketing & Content Strategy Intern</div>
      <div class="tl-company">Colley — IP licensing &amp; fandom commerce platform</div>
      <div class="tl-period">MAY – AUG 2021</div>
      <div class="bul">Increased user retention by <b>40%</b> via personalized push notification strategy; experience in IP monetization and community-driven retail ecosystems</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

# ─── KEY PROJECTS ─────────────────────────────────────────────
with t_projects:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Highlights</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Key Projects</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-desc">End-to-end ownership, measurable impact, national media reach.</div>', unsafe_allow_html=True)

    st.markdown('<div class="proj-grid">', unsafe_allow_html=True)
    st.markdown("""
    <div class="proj-card">
      <div class="proj-no">01</div>
      <div class="proj-title">Built-in Kitchen Zone — Jamsil</div>
      <div class="proj-sub">Opening May 2026 · Gaggenau · Liebherr · Fhiaba · 9-month program</div>
      <div class="proj-badges">
        <span class="proj-badge">3 Global Brands</span>
        <span class="proj-badge">Korea First</span>
        <span class="proj-badge">Sep 2024 → May 2026</span>
      </div>
      <div class="proj-bul">Led full lifecycle from initial planning through construction and coordinated multi-brand opening</div>
      <div class="proj-bul"><b>Primary liaison</b> between global brands, internal design teams, and construction vendors — resolved fixture/logo spec conflicts</div>
      <div class="proj-bul">Designed <b>repeat-visit engagement programs</b> (cooking classes, private events) to convert high-consideration shoppers</div>
    </div>

    <div class="proj-card">
      <div class="proj-no">02</div>
      <div class="proj-title">Asahi Super Dry Pop-up</div>
      <div class="proj-sub">Korea's first retail activation of this kind · 14 days · Zero paid media</div>
      <div class="proj-badges">
        <span class="proj-badge">$120K Revenue</span>
        <span class="proj-badge">6,000 Transactions</span>
        <span class="proj-badge">1,300+ New Customers</span>
        <span class="proj-badge">13 Press Features</span>
      </div>
      <div class="proj-bul">Proactively identified issue, secured exclusive pop-up rights; crafted limited-release activation for peak sell-through</div>
      <div class="proj-bul">Organic coverage by @busanunnie (355K followers) — <b>became internal company benchmark</b></div>
    </div>

    <div class="proj-card">
      <div class="proj-no">03</div>
      <div class="proj-title">Dongdaemun District Renewal</div>
      <div class="proj-sub">Daiso + Whose Fan Café · Foreign visitor data strategy</div>
      <div class="proj-badges">
        <span class="proj-badge">₩26.7억 Revenue</span>
        <span class="proj-badge">₩1.8억 Profit</span>
        <span class="proj-badge">Daiso ₩25억 Annual</span>
      </div>
      <div class="proj-bul">District-level demand analysis using foreign visitor traffic data — identified unmet demand for value retail + K-POP fandom café</div>
      <div class="proj-bul">Recruited both tenants; managed full onboarding; Whose Fan Café launched artist events and K-Dessert concept — first of its kind in channel</div>
    </div>

    <div class="proj-card">
      <div class="proj-no">04</div>
      <div class="proj-title">Naver Eohakdang Content Strategy</div>
      <div class="proj-sub">Data-driven content curation · 3-month sprint</div>
      <div class="proj-badges">
        <span class="proj-badge">+30% Daily Views</span>
        <span class="proj-badge">CTR 1.5× Boost</span>
        <span class="proj-badge">3 Interventions</span>
      </div>
      <div class="proj-bul">Diagnosed &lt;1 daily view/user problem via 6-month data analysis; identified format preferences and peak engagement timing</div>
      <div class="proj-bul">Rebalanced content mix, produced spoken-English series, placed quiz at commute-hour top slot — <b>+30% daily views in 3 months</b></div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

# ─── SKILLS ───────────────────────────────────────────────────
with t_skills:
    st.markdown('<div class="section-gray">', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Capabilities</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Core Competencies</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        for cat, skills in [
            ("Commercial & Financial", ["P&L Management", "Category Strategy & KPI Definition", "Margin Optimization", "Portfolio Rebalancing", "Pricing & Promotional ROI", "Financial Modeling (Excel)"]),
            ("Activation & Merchandising", ["Pop-Up & Brand Activation", "IP Retail Program Management", "Influencer-Linked Commerce", "Visual Merchandising", "Traffic-Driving Events", "Online + Offline Integration"]),
        ]:
            tags = "".join(f'<span class="skill-tag">{s}</span>' for s in skills)
            st.markdown(f'<div class="skill-block"><div class="skill-cat-title">{cat}</div><div class="skill-tags">{tags}</div></div>', unsafe_allow_html=True)

    with col2:
        for cat, skills in [
            ("Vendor & Negotiation", ["Vendor Relationship Management", "Commercial Term Restructuring", "Joint Business Planning (JBP)", "Tenant Replacement Strategy", "Lease Negotiation", "New Brand Sourcing"]),
            ("Analytics & Tools", ["Advanced Excel (Pivot, VLOOKUP, Scenario Analysis)", "Large Dataset Analysis", "Sell-Through & Inventory Monitoring", "Consumer Insights", "AI Tools Integration", "Cross-Functional Coordination"]),
        ]:
            tags = "".join(f'<span class="skill-tag">{s}</span>' for s in skills)
            st.markdown(f'<div class="skill-block"><div class="skill-cat-title">{cat}</div><div class="skill-tags">{tags}</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ─── EDUCATION ────────────────────────────────────────────────
with t_edu:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Academic</div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-title">Education</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="edu-card">
      <div class="edu-icon">🎓</div>
      <div>
        <div class="edu-degree">B.A. in European Culture &amp; Russian Studies</div>
        <div class="edu-school">Chung-Ang University, Seoul</div>
        <div class="edu-period">MAR 2017 – AUG 2021</div>
        <div class="bul">Selected coursework in Business &amp; Finance: Marketing, Corporate Finance, Managerial Accounting, Consumer Behavior, Organizational Behavior, International Business</div>
      </div>
    </div>
    <div class="edu-card">
      <div class="edu-icon">✈️</div>
      <div>
        <div class="edu-degree">Exchange Student</div>
        <div class="edu-school">Higher School of Economics (HSE), St. Petersburg, Russia</div>
        <div class="edu-period">2020 EXCHANGE SEMESTER</div>
        <div class="bul">Economics and Business track; international academic experience at one of Russia's leading research universities</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ─── FOOTER ───────────────────────────────────────────────────
st.markdown(f"""
<div class="footer">
  <div>
    <div class="footer-name">Jiwon Kim</div>
    <div class="footer-sub">Retail Buyer &amp; Brand Activator · South Korea</div>
  </div>
  <div class="footer-links">
    <a class="footer-link" href="mailto:jiwonkimv@gmail.com">jiwonkimv@gmail.com</a>
    <a class="footer-link" href="tel:+821026573623">(+82) 10-2657-3623</a>
    <a class="share-btn" href="{linkedin}" target="_blank">🔗 LinkedIn Profile</a>
  </div>
</div>
""", unsafe_allow_html=True)
