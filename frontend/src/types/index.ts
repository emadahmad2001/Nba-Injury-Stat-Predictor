export interface Player {
  id: number;
  name: string;
  team: string;
  position: string;
  points_per_game: number;
  rebounds_per_game: number;
  assists_per_game: number;
}

export interface RecoveryTime {
  duration: number;
  unit: 'days' | 'weeks' | 'months' | 'years';
}

export interface Injury {
  id: number;
  player_id: string;
  player_name: string;
  injury_type: string;
  severity: 'Low' | 'Medium' | 'High';
  date: string;
  recovery_time: RecoveryTime;
  status: 'Active' | 'Recovered';
}

export interface InjuryPrediction {
  player: Player;
  injury_type: string;
  severity: 'Low' | 'Medium' | 'High';
  impact: {
    points: number;
    rebounds: number;
    assists: number;
    recovery_time: number;
  };
  recommendations: string[];
}

export interface InjuryTrend {
  month: string;
  count: number;
}

export interface PositionBreakdown {
  position: string;
  count: number;
}

export interface SeverityDistribution {
  severity: string;
  count: number;
}

export interface CommonInjury {
  injury_type: string;
  count: number;
}

export interface DashboardStats {
  total_injuries: number;
  active_injuries: number;
  avg_recovery_time: number;
  most_common_injuries: CommonInjury[];
  injury_trends: InjuryTrend[];
  position_breakdown: PositionBreakdown[];
  severity_distribution: SeverityDistribution[];
} 