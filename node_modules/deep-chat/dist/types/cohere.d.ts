import { GenericObject } from './object';
export interface CohereSummarizationConfig {
    model?: string;
    length?: 'auto' | 'short' | 'medium' | 'long';
    format?: 'auto' | 'paragraph' | 'bullets';
    extractiveness?: 'auto' | 'low' | 'medium' | 'high';
    temperature?: number;
    additional_command?: string;
}
export interface CohereGenerateConfig {
    model?: string;
    max_tokens?: number;
    truncate?: 'NONE' | 'START' | 'END';
    temperature?: number;
    k?: number;
    p?: number;
    end_sequences?: string[];
    stop_sequences?: string[];
    frequency_penalty?: number;
    presence_penalty?: number;
    logit_bias?: GenericObject<string | number>;
    preset?: string;
}
export interface CohereChatConfig {
    model?: string;
    temperature?: number;
    prompt_truncation?: 'AUTO' | 'OFF';
    connectors?: {
        id: string;
    }[];
    documents?: {
        title: string;
        snippet: string;
    }[];
}
export interface Cohere {
    chat?: true | CohereChatConfig;
    textGeneration?: true | CohereGenerateConfig;
    summarization?: true | CohereSummarizationConfig;
}
//# sourceMappingURL=cohere.d.ts.map