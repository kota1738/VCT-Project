import json

with open('c:/Users/abdur/Documents/VCT-Project/VCT_Interactive_Explorer.ipynb', encoding='utf-8') as f:
    nb = json.load(f)

new_source = r"""# -- Player Profile Card --
from IPython.display import HTML, display
import ipywidgets as widgets

REGION_COLORS = {'Americas': '#a8d4b0', 'EMEA': '#dfa8a8', 'Pacific': '#a0b8dc', 'CN': '#dcc48a'}
METRICS = ['ACS', 'ADR', 'KAST', 'KPR', 'APR', 'FKPR', 'FDPR', 'HS%']

player_dd = widgets.Dropdown(
    options=sorted(combined_df['Player'].unique()),
    description='Player:',
    layout=widgets.Layout(width='300px')
)
event_dd = widgets.Dropdown(
    options=['All', 'Masters Bangkok 2025', 'Masters Toronto 2025', 'Champions 2025'],
    value='All',
    description='Event:',
    layout=widgets.Layout(width='300px')
)
out_profile = widgets.Output()

def make_card(row, rc, region, reg_avg, show_badge):
    def bar(metric):
        val = float(row[metric]) if pd.notna(row[metric]) else 0
        avg = float(reg_avg[metric]) if pd.notna(reg_avg[metric]) else 0
        mx  = float(combined_df[metric].max()) or 1
        pct = min(val / mx * 100, 100)
        diff = val - avg
        ds = ('+' if diff >= 0 else '') + f'{diff:.2f}'
        dc = '#a8d4b0' if diff >= 0 else '#dfa8a8'
        return f"""<div style='margin-bottom:9px;'>
          <div style='display:flex;justify-content:space-between;margin-bottom:2px;'>
            <span style='color:#aabbcc;font-size:12px;'>{metric}</span>
            <span style='color:#fff;font-size:12px;font-weight:bold;'>{val:.2f} <span style='color:{dc};font-size:11px;'>({ds} vs reg avg)</span></span>
          </div>
          <div style='background:#0f1923;border-radius:4px;height:6px;'>
            <div style='background:{rc};width:{pct:.1f}%;height:6px;border-radius:4px;'></div>
          </div></div>"""

    badge = f"<span style='background:#e08888;color:#0f1923;font-size:11px;font-weight:700;padding:2px 10px;border-radius:20px;display:inline-block;margin-bottom:10px;'>{row['Event']}</span>" if show_badge else ''
    agents = row['Agents'] if pd.notna(row.get('Agents')) else 'N/A'
    kd = row['K:D'] if pd.notna(row.get('K:D')) else 'N/A'

    return f"""<div style='background:#0f1923;border:1px solid #2a3f54;border-radius:12px;font-family:Segoe UI,sans-serif;overflow:hidden;margin-bottom:14px;'>
  <div style='background:linear-gradient(135deg,#1a2535,#0f1923);padding:20px 26px;border-bottom:3px solid {rc};display:flex;align-items:center;gap:18px;'>
    <div style='background:{rc};color:#0f1923;width:50px;height:50px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:900;flex-shrink:0;'>{row['Player'][0].upper()}</div>
    <div>
      <div style='color:#fff;font-size:20px;font-weight:800;'>{row['Player']}</div>
      <div style='color:#8899aa;font-size:13px;'>{row['Team']} &middot; <span style='color:{rc};'>{region}</span></div>
      <div style='color:#aabbcc;font-size:12px;margin-top:3px;'>Agents: {agents} &nbsp;|&nbsp; K/D: {kd} &nbsp;|&nbsp; Rounds: {int(row['Rnd'])}</div>
    </div>
  </div>
  <div style='padding:18px 26px;'>
    {badge}
    <div style='color:#e08888;font-size:11px;letter-spacing:3px;text-transform:uppercase;margin-bottom:12px;'>Metrics vs {region} Average</div>
    {''.join(bar(m) for m in METRICS)}
  </div>
</div>"""

def show_profile(player, event):
    rows = combined_df[combined_df['Player'] == player]
    if event != 'All':
        rows = rows[rows['Event'] == event]
    if rows.empty:
        with out_profile:
            out_profile.clear_output(wait=True)
            display(HTML("<span style='color:#dfa8a8;font-family:Segoe UI;'>No data for this player at the selected event.</span>"))
        return
    region = rows.iloc[0]['Region']
    rc = REGION_COLORS.get(region, '#888')
    reg_avg = combined_df[combined_df['Region'] == region][METRICS].mean()
    multi = len(rows) > 1
    html = ''.join(make_card(row, rc, region, reg_avg, multi) for _, row in rows.iterrows())
    if multi:
        avg = rows[METRICS].mean()
        rows_html = ''.join(f"<div style='display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid #1a2535;'><span style='color:#aabbcc;font-size:12px;'>{m}</span><span style='color:#fff;font-size:12px;font-weight:bold;'>{avg[m]:.2f}</span></div>" for m in METRICS)
        html += f"""<div style='background:#0f1923;border:1px solid #e08888;border-radius:12px;font-family:Segoe UI,sans-serif;overflow:hidden;margin-bottom:14px;'>
  <div style='background:linear-gradient(135deg,#1a2535,#0f1923);padding:16px 26px;border-bottom:2px solid #e08888;'>
    <div style='color:#e08888;font-size:11px;letter-spacing:3px;text-transform:uppercase;'>Overall Average — All Events</div>
    <div style='color:#fff;font-size:16px;font-weight:800;margin-top:4px;'>{player}</div>
  </div>
  <div style='padding:16px 26px;'>{rows_html}</div>
</div>"""
    with out_profile:
        out_profile.clear_output(wait=True)
        display(HTML(f"<div style='max-width:700px;'>{html}</div>"))

def _on_change(change):
    show_profile(player_dd.value, event_dd.value)

player_dd.observe(_on_change, names='value')
event_dd.observe(_on_change, names='value')
show_profile(player_dd.value, event_dd.value)
display(widgets.VBox([widgets.HBox([player_dd, event_dd]), out_profile]))
"""

nb['cells'][37]['source'] = new_source.splitlines(keepends=True)

with open('c:/Users/abdur/Documents/VCT-Project/VCT_Interactive_Explorer.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)
print('Done')
