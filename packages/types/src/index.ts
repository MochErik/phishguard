/**
 * Shared Type Definitions for PhishGuard Ecosystem
 */

export type ScanType = 'url' | 'email' | 'sms' | 'qr' | 'web' | 'document';

export type Verdict = 'safe' | 'suspicious' | 'phishing';

export interface BlacklistCheckResult {
  hit: boolean;
  source: string;
  details?: string;
}

export interface URLFeatures {
  url: string;
  domain: string;
  has_ip: boolean;
  url_entropy: number;
  suspicious_keywords: string[];
  subdomain_count: number;
}

export interface NLPAnalysisResult {
  urgency_score: number;
  threat_score: number;
  reward_score: number;
  flagged_phrases: string[];
}

export interface UnifiedScanResponse {
  scan_id: string;
  scan_type: ScanType;
  verdict: Verdict;
  risk_score: number;
  confidence: number;
  summary: string;
  recommendations: string[];
  url_features?: URLFeatures;
  nlp_result?: NLPAnalysisResult;
  processing_time_ms: number;
  scanned_at: string;
}
