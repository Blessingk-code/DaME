# Data-Aware Metadata Enricher — QGIS Plugin

**Data-Aware Metadata Enricher** is a QGIS plugin that automatically extracts, analyzes, and enriches geospatial metadata from vector and raster datasets. It generates structured metadata outputs (JSON / XML) suitable for data catalogs, FAIR data pipelines, spatial data infrastructures (SDIs), and STAC-based workflows.

The plugin combines geospatial intelligence with optional large language model (LLM) support to produce high-quality, human-readable dataset descriptions.

---

## Key Features

-  Automated extraction of spatial, attribute, and raster metadata
-  Accurate reprojection of spatial extents to WGS84 (EPSG:4326)
- Intelligent summarization of attribute distributions
- Optional LLM-powered field translation and description enhancement
- JSON and XML metadata export
- Fully integrated into the QGIS Processing framework
- One-click execution from the QGIS toolbar

---

## Installation

### Option 1 — From ZIP (Recommended for Development)

1. Download the plugin ZIP archive from GitHub.
2. Open QGIS → **Plugins → Manage and Install Plugins → Install from ZIP**
3. Select the downloaded ZIP file.
4. Enable **Data-Aware Metadata Enricher** from the plugin list.

---

### Option 2 — From QGIS Plugin Repository *(Coming Soon)*

Once published:



## How to Use

### Toolbar Access

Click the **Data-Aware Metadata Enricher** icon in the QGIS toolbar.

This opens the native Processing interface.

---

### Inputs

- **Vector Layer** *(optional)*  
- **Raster Layer** *(optional)*  
- **Metadata File** *(optional JSON or XML input)*
- **Output Metadata File** *(JSON or XML)*  
- **Fields to Scan** *(vector only)*  
- **Sample Size** *(default: 500)*  
- **Use LLM Enhancement** *(optional)*  

---

### Output

The plugin produces structured metadata including:

- Spatial extent (WGS84)
- CRS information
- Geometry type
- Feature count
- Attribute summaries
- Raster statistics (min, max, mean, stddev)
- Human-readable dataset overview
- Provenance information

---

## Example Output (JSON)

```json
{
  "layer_name": "Landcover_2020",
  "crs": "EPSG:4326",
  "spatial": {
    "xmin": 11.42,
    "ymin": 48.02,
    "xmax": 11.71,
    "ymax": 48.23
  },
  "feature_count": 124392,
  "fields_summary": {
    "class": {
      "type": "categorical",
      "unique_values": 12
    }
  },
  "descriptive_overview": "This dataset represents land cover classes derived from remote sensing imagery..."
}


##License

This project is licensed under the MIT License — see the LICENSE file for details.


##Citation

If you use this plugin in academic work, please cite:

Kavhu, B. (2026). Data-Aware Metadata Enricher: Intelligent Metadata Generation for Geospatial Data in QGIS.


##Contributing

Pull requests, feature suggestions, and collaborations are very welcome.


##Contact

Author: Blessing Kavhu
Affiliation: Senior Researcher / MML
GitHub: https://github.com/yourusername
