/**
 * @phishguard/core — Shared Phishing Heuristics & Scoring Functions
 */

export const RISK_THRESHOLDS = {
  SAFE: 0.30,
  SUSPICIOUS: 0.65,
  PHISHING: 1.00,
};

export function calculateEntropy(input: string): number {
  if (!input) return 0;
  const map: Record<string, number> = {};
  for (let i = 0; i < input.length; i++) {
    const c = input[i];
    map[c] = (map[c] || 0) + 1;
  }
  let entropy = 0;
  for (const c in map) {
    const p = map[c] / input.length;
    entropy -= p * Math.log2(p);
  }
  return Number(entropy.toFixed(3));
}

export function determineVerdict(score: number): 'safe' | 'suspicious' | 'phishing' {
  if (score >= RISK_THRESHOLDS.SUSPICIOUS) return 'phishing';
  if (score >= RISK_THRESHOLDS.SAFE) return 'suspicious';
  return 'safe';
}

export const SECURITY_WEIGHTS = {
  BLACKLIST: 0.40,
  URL_HEURISTICS: 0.25,
  NLP_SOCIAL_ENGINEERING: 0.25,
  AI_MODEL: 0.10,
};
