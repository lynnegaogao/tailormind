export interface AzureTranslationConfig {
    language?: string;
}
export interface AzureSummarizationConfig {
    language?: string;
}
export interface AzureEndpoint {
    endpoint: string;
}
export interface AzureSpeechToTextConfig {
    lang?: string;
}
export interface AzureTextToSpeechConfig {
    lang?: string;
    name?: string;
    gender?: string;
    outputFormat?: string;
}
export interface AzureRegion {
    region: string;
}
export interface Azure {
    textToSpeech?: AzureRegion & AzureTextToSpeechConfig;
    speechToText?: AzureRegion & AzureSpeechToTextConfig;
    summarization?: AzureEndpoint & AzureSummarizationConfig;
    translation?: Partial<AzureRegion> & AzureTranslationConfig;
}
//# sourceMappingURL=azure.d.ts.map