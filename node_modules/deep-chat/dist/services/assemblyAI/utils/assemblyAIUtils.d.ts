import { KeyVerificationDetails } from '../../../types/keyVerificationDetails';
export declare class AssemblyAIUtils {
    static poll(api_token: string, audio_url: string): Promise<{
        text: string;
    }>;
    static buildHeaders(key: string): {
        Authorization: string;
        'Content-Type': string;
    };
    private static handleVerificationResult;
    static buildKeyVerificationDetails(): KeyVerificationDetails;
}
//# sourceMappingURL=assemblyAIUtils.d.ts.map