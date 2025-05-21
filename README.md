# NBA Injury Stat Predictor 2025 🏀

An advanced analytics dashboard for predicting NBA player performance after injuries, featuring real-time data visualization and machine learning predictions.

## Features

### 1. Player Performance Prediction
- Predict post-injury performance for NBA players
- Support for multiple injury types (ankle, knee, hamstring, etc.)
- Customizable recovery time input
- Real-time performance metrics calculation

### 2. Advanced Visualizations
- **Shot Chart Heatmap**: Visual representation of player shooting patterns
- **Player Efficiency Radar**: Multi-dimensional performance metrics
- **League Trend Sparklines**: Year-over-year statistical comparisons

### 3. 2025 Player Database
- Updated roster with current NBA stars
- Comprehensive player statistics
- Team affiliations and injury history

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Visualization**: Canvas API for custom charts
- **Data Sources**: NBA.com, Basketball-Reference.com

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nba-injury-stat-predictor.git
cd nba-injury-stat-predictor
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

4. Open your browser and navigate to `http://localhost:3000`

## Project Structure

```
nba-injury-stat-predictor/
├── frontend/
│   ├── components/
│   │   ├── ShotChart.js
│   │   ├── RadarChart.js
│   │   ├── TrendGraph.js
│   │   └── HomeTab.js
│   ├── data/
│   │   └── players.json
│   ├── styles.css
│   └── index.html
├── backend/
│   └── main.py
└── README.md
```

## Data Sources

- Player Statistics: NBA.com/stats
- Shot Charts: NBA.com/statshotcharts
- League Trends: basketball-reference.com/leagues/NBA_2025

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## Acknowledgments

- NBA.com for providing comprehensive statistics
- Basketball-Reference.com for historical data
- All contributors who have helped improve this project
