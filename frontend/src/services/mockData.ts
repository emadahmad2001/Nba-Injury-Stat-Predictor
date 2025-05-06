import { Player, DashboardStats, InjuryTrend, PositionBreakdown, SeverityDistribution, CommonInjury } from '../types';

export const mockPlayers: Player[] = [
  {
    id: 1,
    name: 'LeBron James',
    team: 'Los Angeles Lakers',
    position: 'SF',
    points_per_game: 25.7,
    rebounds_per_game: 7.2,
    assists_per_game: 7.9
  },
  {
    id: 2,
    name: 'Stephen Curry',
    team: 'Golden State Warriors',
    position: 'PG',
    points_per_game: 29.4,
    rebounds_per_game: 4.4,
    assists_per_game: 6.3
  },
  {
    id: 3,
    name: 'Joel Embiid',
    team: 'Philadelphia 76ers',
    position: 'C',
    points_per_game: 33.1,
    rebounds_per_game: 11.4,
    assists_per_game: 6.0
  },
  {
    id: 4,
    name: 'Nikola Jokic',
    team: 'Denver Nuggets',
    position: 'C',
    points_per_game: 24.5,
    rebounds_per_game: 12.3,
    assists_per_game: 9.0
  },
  {
    id: 5,
    name: 'Luka Doncic',
    team: 'Dallas Mavericks',
    position: 'PG',
    points_per_game: 32.2,
    rebounds_per_game: 9.2,
    assists_per_game: 9.8
  }
];

export const mockDashboardStats: DashboardStats = {
  total_injuries: 42,
  active_injuries: 15,
  avg_recovery_time: 12.5,
  most_common_injuries: [
    { injury_type: 'Ankle Sprain', count: 12 },
    { injury_type: 'Knee Contusion', count: 8 },
    { injury_type: 'Hamstring Strain', count: 6 },
    { injury_type: 'Back Sprain', count: 5 },
    { injury_type: 'Shoulder Impingement', count: 4 }
  ],
  injury_trends: [
    { month: 'Jan', count: 8 },
    { month: 'Feb', count: 12 },
    { month: 'Mar', count: 15 },
    { month: 'Apr', count: 7 }
  ],
  position_breakdown: [
    { position: 'PG', count: 8 },
    { position: 'SG', count: 6 },
    { position: 'SF', count: 10 },
    { position: 'PF', count: 9 },
    { position: 'C', count: 9 }
  ],
  severity_distribution: [
    { severity: 'Low', count: 20 },
    { severity: 'Medium', count: 15 },
    { severity: 'High', count: 7 }
  ]
}; 