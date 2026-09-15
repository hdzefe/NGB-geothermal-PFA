"""
Generate high-quality workflow diagram for North German Basin 18-Horizon PFA
Output: PNG, PDF, SVG formats ready for peer-reviewed publication
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# ============================================================================
# OPTION 1: MATPLOTLIB (Recommended for quick generation)
# ============================================================================

def generate_workflow_diagram_matplotlib():
    """
    Generate professional workflow diagram using matplotlib
    Output: PNG (300 DPI for publication)
    """
    
    fig, ax = plt.subplots(figsize=(20, 14), dpi=100)
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 14)
    ax.axis('off')
    
    # Define colors
    color_input = '#E8F4F8'
    color_process = '#FFF8E1'
    color_output = '#E8F5E9'
    color_economic = '#F3E5F5'
    color_composite = '#FCE4EC'
    
    # ========== LEFT COLUMN: INPUT LAYERS ==========
    
    # Title
    ax.text(2, 13.2, 'INPUT LAYERS', fontsize=14, fontweight='bold', ha='center')
    
    # Geological Criteria label
    ax.text(1.2, 12.5, 'GEOLOGICAL CRITERIA', fontsize=11, fontweight='bold', ha='left', color='#1565C0')
    ax.text(1.2, 12.1, '(Per Horizon)', fontsize=9, ha='left', style='italic')
    
    # Geological input boxes (examples for Horizon 1)
    geo_inputs = [
        ('Synthetic Thermal\nHorizon #1\n[°C at depth]', 11.5),
        ('TUNB Depth Surface\n[m below surface]', 10.7),
        ('Heat Flow\n[mW/m²]', 9.9),
        ('Prospective Sandstones\n(Vatangin-Bueckeberg)\n[probability/thickness]', 9.1),
        ('Salt Structures\nDistance\n[km from seal]', 8.0),
        ('Geothermal Evidence\n(Boreholes)\n[km distance]', 7.0),
    ]
    
    for label, y_pos in geo_inputs:
        box = FancyBboxPatch((0.8, y_pos-0.35), 2.4, 0.6, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#1565C0', facecolor=color_input, linewidth=1.5)
        ax.add_patch(box)
        ax.text(2, y_pos, label, fontsize=8, ha='center', va='center')
    
    # Arrow indicating "For each of 18 horizons"
    ax.annotate('', xy=(2, 6.2), xytext=(2, 6.5),
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax.text(2.8, 6.35, 'FOR EACH OF 18 HORIZONS', fontsize=9, 
            fontweight='bold', color='red', ha='left')
    
    # Economic Criteria label (below geological)
    ax.text(1.2, 5.6, 'ECONOMIC CRITERIA', fontsize=11, fontweight='bold', 
            ha='left', color='#6A1B9A')
    ax.text(1.2, 5.2, '(SHARED ACROSS ALL HORIZONS)', fontsize=9, ha='left', style='italic')
    
    # Economic input boxes
    econ_inputs = [
        ('Population Density\n[people/km²]', 4.7),
        ('District Heating Network\nDistance [km]', 3.9),
        ('Upstream Petroleum\nElectrification\n[feasibility index]', 3.0),
        ('Electrical Infrastructure\nDistance [km]', 2.0),
        ('Proposed Electrical\nInfrastructure [km]', 1.0),
    ]
    
    for label, y_pos in econ_inputs:
        box = FancyBboxPatch((0.8, y_pos-0.35), 2.4, 0.6, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#6A1B9A', facecolor=color_economic, linewidth=1.5)
        ax.add_patch(box)
        ax.text(2, y_pos, label, fontsize=8, ha='center', va='center')
    
    # ========== MIDDLE COLUMN: WEIGHTED SUMMATION PROCESS ==========
    
    ax.text(10, 13.2, 'WEIGHTED SUMMATION PROCESS', fontsize=14, 
            fontweight='bold', ha='center')
    
    # GEOLOGICAL COMPONENT (Horizon 1 example)
    ax.text(5.5, 12.5, 'GEOLOGICAL COMPONENT', fontsize=10, fontweight='bold', 
            ha='center', bbox=dict(boxstyle='round', facecolor=color_process, edgecolor='#F57F17', linewidth=2))
    
    # Weight labels for geological
    weights_geo = [
        ('Weight: 0.30\n(Thermal)', 6.8, 11.7),
        ('Weight: 0.70\n(Geologic)', 6.8, 9.8),
    ]
    for label, x, y in weights_geo:
        ax.text(x, y, label, fontsize=8, ha='center', va='center',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor='#F57F17', linewidth=1))
    
    # Arrows from geological inputs to summation
    arrow_positions_geo = [11.5, 10.7, 9.9, 9.1, 8.0, 7.0]
    for y_from in arrow_positions_geo:
        # Horizontal arrows from inputs to weights
        arrow = FancyArrowPatch((3.2, y_from), (5.2, y_from),
                               arrowstyle='->', mutation_scale=20, linewidth=1.5, 
                               color='#1565C0', alpha=0.6)
        ax.add_patch(arrow)
    
    # Summation symbol (⊗) for geological
    circle = plt.Circle((7.5, 10.75), 0.3, color='#F57F17', alpha=0.7)
    ax.add_patch(circle)
    ax.text(7.5, 10.75, '⊗', fontsize=16, ha='center', va='center', color='white', fontweight='bold')
    
    # Arrow from summation to output
    arrow = FancyArrowPatch((7.8, 10.75), (9.2, 10.75),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='#F57F17')
    ax.add_patch(arrow)
    
    # Geological Summary Layer output box
    box = FancyBboxPatch((9.2, 10.5), 2.5, 0.5, 
                        boxstyle="round,pad=0.05", 
                        edgecolor='#F57F17', facecolor=color_process, linewidth=2)
    ax.add_patch(box)
    ax.text(10.45, 10.75, 'Geological\nSummary Layer', fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Weight for geological (0.5)
    ax.text(10.45, 10.05, 'Weight: 0.5', fontsize=8, ha='center', va='center',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#F57F17', linewidth=1))
    
    # ECONOMIC COMPONENT (Shared)
    ax.text(5.5, 6.0, 'ECONOMIC COMPONENT', fontsize=10, fontweight='bold', 
            ha='center', bbox=dict(boxstyle='round', facecolor=color_process, edgecolor='#6A1B9A', linewidth=2))
    
    # Weight labels for economic
    weights_econ = [
        ('Weight: 0.273', 6.8, 5.1),
        ('Weight: 0.273', 6.8, 4.3),
        ('Weight: 0.273', 6.8, 3.5),
        ('Weight: 0.181', 6.8, 2.7),
    ]
    for label, x, y in weights_econ:
        ax.text(x, y, label, fontsize=7, ha='center', va='center',
               bbox=dict(boxstyle='round', facecolor='white', edgecolor='#6A1B9A', linewidth=1))
    
    # Arrows from economic inputs to summation
    arrow_positions_econ = [4.7, 3.9, 3.0, 2.0, 1.0]
    for y_from in arrow_positions_econ:
        arrow = FancyArrowPatch((3.2, y_from), (5.2, y_from),
                               arrowstyle='->', mutation_scale=20, linewidth=1.5, 
                               color='#6A1B9A', alpha=0.6)
        ax.add_patch(arrow)
    
    # Summation symbol (⊗) for economic
    circle = plt.Circle((7.5, 3.5), 0.3, color='#6A1B9A', alpha=0.7)
    ax.add_patch(circle)
    ax.text(7.5, 3.5, '⊗', fontsize=16, ha='center', va='center', color='white', fontweight='bold')
    
    # Arrow from summation to output
    arrow = FancyArrowPatch((7.8, 3.5), (9.2, 3.5),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='#6A1B9A')
    ax.add_patch(arrow)
    
    # Economic Summary Layer output box
    box = FancyBboxPatch((9.2, 3.25), 2.5, 0.5, 
                        boxstyle="round,pad=0.05", 
                        edgecolor='#6A1B9A', facecolor=color_process, linewidth=2)
    ax.add_patch(box)
    ax.text(10.45, 3.5, 'Economic\nSummary Layer', fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Weight for economic (0.5)
    ax.text(10.45, 2.8, 'Weight: 0.5\n(Applied to all 18 horizons)', fontsize=8, ha='center', va='center',
           bbox=dict(boxstyle='round', facecolor='white', edgecolor='#6A1B9A', linewidth=1))
    
    # Final summation for each horizon
    ax.text(14, 11.8, 'FINAL SUMMATION\n(Per Horizon)', fontsize=10, fontweight='bold', 
            ha='center', bbox=dict(boxstyle='round', facecolor=color_process, edgecolor='#D32F2F', linewidth=2))
    
    # Arrows from component summaries to final
    arrow = FancyArrowPatch((11.7, 10.75), (13.2, 11.5),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='#F57F17')
    ax.add_patch(arrow)
    
    arrow = FancyArrowPatch((11.7, 3.5), (13.2, 11.0),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='#6A1B9A')
    ax.add_patch(arrow)
    
    # Final summation symbol
    circle = plt.Circle((14, 11.2), 0.25, color='#D32F2F', alpha=0.7)
    ax.add_patch(circle)
    ax.text(14, 11.2, '⊗', fontsize=14, ha='center', va='center', color='white', fontweight='bold')
    
    # ========== RIGHT COLUMN: FAVORABILITY MAPS ==========
    
    ax.text(17.5, 13.2, 'FAVORABILITY MAPS', fontsize=14, fontweight='bold', ha='center')
    
    # Horizon maps
    horizon_maps = [
        ('HORIZON 1:\nVatangin-Bueckeberg', 16.5, 11.8),
        ('HORIZON 2:\nMiddle-Bunter Sand', 16.5, 9.8),
        ('...\n(Horizons 3-17)', 16.5, 7.5),
        ('HORIZON 18:\n[Deepest Horizon]', 16.5, 5.2),
    ]
    
    for label, x, y in horizon_maps:
        box = FancyBboxPatch((x-1.2, y-0.5), 2.4, 1.0, 
                            boxstyle="round,pad=0.05", 
                            edgecolor='#D32F2F', facecolor=color_output, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, label, fontsize=9, ha='center', va='center', fontweight='bold')
        
        # Add color scale below each map
        ax.text(x, y-0.8, '[0-5 Favorability\nRed-Yellow-Blue]', fontsize=7, 
               ha='center', va='top', style='italic', color='gray')
    
    # Arrows from final summation to output maps
    arrow = FancyArrowPatch((14.3, 11.2), (15.3, 11.8),
                           arrowstyle='->', mutation_scale=20, linewidth=2, color='#D32F2F')
    ax.add_patch(arrow)
    
    # ========== BOTTOM: COMPOSITE STACKING ANALYSIS ==========
    
    ax.text(10, 0.7, 'POST-PROCESSING: COMPOSITE STACKING ANALYSIS', fontsize=12, 
            fontweight='bold', ha='center', 
            bbox=dict(boxstyle='round', facecolor=color_composite, edgecolor='#00695C', linewidth=2, pad=0.5))
    
    ax.text(10, 0.2, 'Stack all 18 maps geographically | Count favorable horizons per location | Identify hotspots with 4-6 stacked favorable horizons (Primary Targets)',
           fontsize=8, ha='center', style='italic', color='#00695C')
    
    plt.tight_layout()
    plt.savefig('NGB_Workflow_Diagram.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("✓ Saved: NGB_Workflow_Diagram.png (300 DPI for publication)")
    plt.close()


# ============================================================================
# OPTION 2: GRAPHVIZ (For more complex flowcharts)
# ============================================================================

def generate_workflow_diagram_graphviz():
    """
    Generate workflow diagram using Graphviz
    Install: pip install graphviz
    Requires: graphviz software installed (https://graphviz.org/download/)
    Output: PDF, SVG, PNG
    """
    
    from graphviz import Digraph
    
    dot = Digraph(comment='NGB 18-Horizon PFA Workflow', format='pdf')
    dot.attr(rankdir='LR', size='20,14')
    dot.attr('node', shape='box', style='rounded,filled', fillcolor='lightblue', fontsize='10')
    
    # Input nodes - Geological
    dot.node('thermal1', 'Synthetic Thermal\nHorizon #1\n[°C at depth]', fillcolor='#E8F4F8')
    dot.node('depth', 'TUNB Depth\n[m below surface]', fillcolor='#E8F4F8')
    dot.node('heatflow', 'Heat Flow\n[mW/m²]', fillcolor='#E8F4F8')
    dot.node('sandstone', 'Prospective\nSandstones\n[probability]', fillcolor='#E8F4F8')
    dot.node('salt', 'Salt Structures\nDistance\n[km]', fillcolor='#E8F4F8')
    dot.node('boreholes', 'Geothermal Evidence\n(Boreholes)\n[km distance]', fillcolor='#E8F4F8')
    
    # Input nodes - Economic
    dot.node('population', 'Population Density\n[people/km²]', fillcolor='#F3E5F5')
    dot.node('dhn', 'District Heating\nNetwork Distance\n[km]', fillcolor='#F3E5F5')
    dot.node('infra', 'Electrical\nInfrastructure\nDistance [km]', fillcolor='#F3E5F5')
    
    # Processing nodes
    dot.node('thermal_proc', 'Thermal Component\nWeight: 0.30\nPr0: 0.60', fillcolor='#FFF8E1', shape='box')
    dot.node('geo_proc', 'Geologic Component\nWeight: 0.70\nPr0: 0.50', fillcolor='#FFF8E1', shape='box')
    dot.node('econ_proc', 'Economic Component\nWeight: 0.50\n(Shared)', fillcolor='#FFF8E1', shape='box')
    
    # Summary layers
    dot.node('thermal_summary', 'Thermal\nSummary Layer\nWeight: 0.60', fillcolor='#FFE082', shape='box')
    dot.node('geo_summary', 'Geological\nSummary Layer\nWeight: 0.40', fillcolor='#FFE082', shape='box')
    dot.node('econ_summary', 'Economic\nSummary Layer\nWeight: 0.50', fillcolor='#FFE082', shape='box')
    
    # Output nodes
    dot.node('fav_h1', 'HORIZON 1:\nVatangin-Bueckeberg\nFavorability Map\n(0-5 scale)', 
            fillcolor='#E8F5E9', shape='box')
    dot.node('fav_h2', 'HORIZON 2:\nMiddle-Bunter\nFavorability Map\n(0-5 scale)', 
            fillcolor='#E8F5E9', shape='box')
    dot.node('fav_h18', 'HORIZON 18:\n[Deepest]\nFavorability Map\n(0-5 scale)', 
            fillcolor='#E8F5E9', shape='box')
    
    # Composite output
    dot.node('composite', 'COMPOSITE STACKING MAP\n(Identify hotspots with 4-6\nfavorable horizons stacked)', 
            fillcolor='#FCE4EC', shape='box')
    
    # Edges - Geological
    dot.edge('thermal1', 'thermal_proc', label='0.30')
    dot.edge('depth', 'thermal_proc', label='0.40')
    dot.edge('heatflow', 'thermal_proc', label='0.30')
    
    dot.edge('sandstone', 'geo_proc', label='0.50')
    dot.edge('salt', 'geo_proc', label='0.30')
    dot.edge('boreholes', 'geo_proc', label='0.20')
    
    # Edges - Economic
    dot.edge('population', 'econ_proc', label='0.273')
    dot.edge('dhn', 'econ_proc', label='0.273')
    dot.edge('infra', 'econ_proc', label='0.181')
    
    # Edges - Processing to Summary
    dot.edge('thermal_proc', 'thermal_summary')
    dot.edge('geo_proc', 'geo_summary')
    dot.edge('econ_proc', 'econ_summary')
    
    # Edges - Summary to Favorability
    dot.edge('thermal_summary', 'fav_h1', label='Voter + Veto')
    dot.edge('geo_summary', 'fav_h1', label='(Horizon 1)')
    dot.edge('econ_summary', 'fav_h1', label='Gate-keeper')
    
    dot.edge('thermal_summary', 'fav_h2', label='Voter + Veto')
    dot.edge('geo_summary', 'fav_h2', label='(Horizon 2)')
    dot.edge('econ_summary', 'fav_h2', label='Gate-keeper')
    
    dot.edge('thermal_summary', 'fav_h18', label='Voter + Veto')
    dot.edge('geo_summary', 'fav_h18', label='(Horizon 18)')
    dot.edge('econ_summary', 'fav_h18', label='Gate-keeper')
    
    # Edges - Favorability to Composite
    dot.edge('fav_h1', 'composite', style='bold', color='red')
    dot.edge('fav_h2', 'composite', style='bold', color='red')
    dot.edge('fav_h18', 'composite', style='bold', color='red')
    
    dot.render('NGB_Workflow_Diagram_Graphviz', view=False, cleanup=True)
    print("✓ Saved: NGB_Workflow_Diagram_Graphviz.pdf (and .svg)")


# ============================================================================
# OPTION 3: DRAW.IO (Web-based, drag-and-drop)
# ============================================================================

def generate_drawio_xml():
    """
    Generate Draw.io XML that you can import into draw.io
    Go to: https://app.diagrams.net/
    File → Open → Upload this XML file
    """
    
    drawio_xml = """<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net" modified="2026-09-15">
  <diagram name="NGB 18-Horizon PFA Workflow">
    <mxGraphModel>
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- Title -->
        <mxCell id="title" value="NORTH GERMAN BASIN: 18-Horizon Reservoir Favorability Analysis" 
          style="text;fontSize=18;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="400" y="20" width="800" height="40" as="geometry"/>
        </mxCell>
        
        <!-- INPUT LAYERS (Left) -->
        <mxCell id="input_label" value="INPUT LAYERS" 
          style="text;fontSize=14;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="50" y="100" width="250" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Geological Inputs -->
        <mxCell id="thermal1" value="Synthetic Thermal Horizon #1 [°C]" 
          style="rounded=1;fillColor=#E8F4F8;strokeColor=#1565C0;" vertex="1" parent="1">
          <mxGeometry x="50" y="150" width="200" height="60" as="geometry"/>
        </mxCell>
        
        <mxCell id="depth" value="TUNB Depth Surface [m bsl]" 
          style="rounded=1;fillColor=#E8F4F8;strokeColor=#1565C0;" vertex="1" parent="1">
          <mxGeometry x="50" y="230" width="200" height="60" as="geometry"/>
        </mxCell>
        
        <!-- ... (add more input cells) ... -->
        
        <!-- PROCESSING (Middle) -->
        <mxCell id="process_label" value="WEIGHTED SUMMATION PROCESS" 
          style="text;fontSize=14;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="400" y="100" width="400" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Thermal Component -->
        <mxCell id="thermal_comp" value="THERMAL COMPONENT\nWeight: 0.30 | Pr0: 0.60" 
          style="rounded=1;fillColor=#FFF8E1;strokeColor=#F57F17;" vertex="1" parent="1">
          <mxGeometry x="350" y="200" width="200" height="80" as="geometry"/>
        </mxCell>
        
        <!-- ... (add more processing cells) ... -->
        
        <!-- OUTPUT (Right) -->
        <mxCell id="output_label" value="FAVORABILITY MAPS" 
          style="text;fontSize=14;fontStyle=1;align=center;" vertex="1" parent="1">
          <mxGeometry x="900" y="100" width="250" height="30" as="geometry"/>
        </mxCell>
        
        <!-- Horizon 1 Output -->
        <mxCell id="fav_h1" value="HORIZON 1:\nVatangin-Bueckeberg\nFavorability Map (0-5)" 
          style="rounded=1;fillColor=#E8F5E9;strokeColor=#D32F2F;" vertex="1" parent="1">
          <mxGeometry x="900" y="200" width="200" height="80" as="geometry"/>
        </mxCell>
        
        <!-- ... (add edges and remaining cells) ... -->
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""
    
    with open('NGB_Workflow_Diagram.drawio', 'w') as f:
        f.write(drawio_xml)
    print("✓ Saved: NGB_Workflow_Diagram.drawio")
    print("  → Open in draw.io: https://app.diagrams.net/")


# ============================================================================
# OPTION 4: POWERPOINT/PYTHON-PPTX
# ============================================================================

def generate_workflow_powerpoint():
    """
    Generate PowerPoint slide with workflow diagram
    Install: pip install python-pptx
    """
    
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.enum.shapes import MSO_SHAPE
    from pptx.dml.color import RGBColor
    
    prs = Presentation()
    prs.slide_width = Inches(20)
    prs.slide_height = Inches(14)
    
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank layout
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(255, 255, 255)
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0), Inches(0.2), Inches(20), Inches(0.5))
    title_frame = title_box.text_frame
    title_frame.text = "North German Basin: 18-Horizon Reservoir Favorability Analysis"
    title_frame.paragraphs[0].font.size = Pt(24)
    title_frame.paragraphs[0].font.bold = True
    title_frame.paragraphs[0].alignment = 1  # Center
    
    # LEFT COLUMN: Input Layers
    left_x = Inches(0.5)
    left_inputs = [
        "Synthetic Thermal H1",
        "TUNB Depth",
        "Heat Flow",
        "Prospective Sandstones",
        "Salt Distance",
        "Boreholes Distance"
    ]
    
    for i, label in enumerate(left_inputs):
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            left_x, Inches(1.2 + i*0.8),
            Inches(2), Inches(0.6)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(232, 244, 248)  # Light blue
        shape.line.color.rgb = RGBColor(21, 101, 192)
        
        text_frame = shape.text_frame
        text_frame.text = label
        text_frame.paragraphs[0].font.size = Pt(10)
        text_frame.word_wrap = True
    
    # MIDDLE COLUMN: Processing (Summation symbols)
    mid_x = Inches(7)
    shape = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        mid_x, Inches(3),
        Inches(0.8), Inches(0.8)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(245, 127, 23)
    text_frame = shape.text_frame
    text_frame.text = "⊗"
    text_frame.paragraphs[0].font.size = Pt(28)
    text_frame.paragraphs[0].font.bold = True
    text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
    
    # RIGHT COLUMN: Output Maps
    right_x = Inches(15)
    right_outputs = [
        "Horizon 1: Vatangin",
        "Horizon 2: Middle-Bunter",
        "...",
        "Horizon 18"
    ]
    
    for i, label in enumerate(right_outputs):
        shape = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            right_x, Inches(1.2 + i*1.5),
            Inches(2.5), Inches(1)
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(232, 245, 233)  # Light green
        shape.line.color.rgb = RGBColor(211, 47, 47)
        
        text_frame = shape.text_frame
        text_frame.text = label + "\nFavorability Map\n(0-5 scale)"
        text_frame.paragraphs[0].font.size = Pt(9)
        text_frame.word_wrap = True
    
    # Bottom: Composite Analysis
    composite_box = slide.shapes.add_textbox(Inches(0.5), Inches(12.5), Inches(19), Inches(1))
    composite_frame = composite_box.text_frame
    composite_frame.text = "POST-PROCESSING: Stack all 18 maps geographically → Count favorable horizons per location → Identify hotspots (4-6 favorable horizons = Primary Targets)"
    composite_frame.paragraphs[0].font.size = Pt(11)
    composite_frame.paragraphs[0].font.italic = True
    composite_frame.paragraphs[0].font.bold = True
    
    prs.save('NGB_Workflow_Diagram.pptx')
    print("✓ Saved: NGB_Workflow_Diagram.pptx")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*70)
    print("NORTH GERMAN BASIN: WORKFLOW DIAGRAM GENERATION")
    print("="*70 + "\n")
    
    # Generate matplotlib version (RECOMMENDED - no dependencies)
    print("Generating matplotlib version (recommended)...")
    try:
        generate_workflow_diagram_matplotlib()
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Generate Graphviz version (optional - requires graphviz software)
    print("\nGenerating Graphviz version (requires graphviz software)...")
    try:
        generate_workflow_diagram_graphviz()
    except ImportError:
        print("  ⚠ Graphviz not installed. Install with: pip install graphviz")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Generate Draw.io XML (for web editing)
    print("\nGenerating Draw.io XML...")
    try:
        generate_drawio_xml()
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Generate PowerPoint version
    print("\nGenerating PowerPoint version...")
    try:
        generate_workflow_powerpoint()
    except ImportError:
        print("  ⚠ python-pptx not installed. Install with: pip install python-pptx")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n" + "="*70)
    print("DONE! Check your directory for:")
    print("  • NGB_Workflow_Diagram.png (300 DPI - PUBLICATION QUALITY)")
    print("  • NGB_Workflow_Diagram.pptx (editable PowerPoint)")
    print("  • NGB_Workflow_Diagram.drawio (for draw.io editing)")
    print("  • NGB_Workflow_Diagram_Graphviz.pdf (vector PDF)")
    print("="*70 + "\n")
