import { KeyVerificationDetails } from '../../../types/keyVerificationDetails';
import { GenericObject } from '../../../types/object';
export declare class AzureUtils {
    static buildTextToSpeechHeaders(outputFormat: string, key: string): {
        'Ocp-Apim-Subscription-Key': string;
        'Content-Type': string;
        'X-Microsoft-OutputFormat': string;
    };
    static buildSpeechToTextHeaders(key: string): {
        'Ocp-Apim-Subscription-Key': string;
        Accept: string;
    };
    private static handleSpeechVerificationResult;
    static buildSpeechKeyVerificationDetails(region: string): KeyVerificationDetails;
    static buildSummarizationHeader(key: string): {
        'Ocp-Apim-Subscription-Key': string;
        'Content-Type': string;
    };
    private static handleLanguageVerificationResult;
    static buildLanguageKeyVerificationDetails(endpoint: string): KeyVerificationDetails;
    private static handleTranslationVerificationResult;
    static buildTranslationKeyVerificationDetails(region?: string): KeyVerificationDetails;
    static buildTranslationHeaders(region: string | undefined, key: string): GenericObject<string>;
}
//# sourceMappingURL=azureUtils.d.ts.map