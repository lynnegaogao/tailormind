import { KeyVerificationDetails } from '../../../types/keyVerificationDetails';
export declare class HuggingFaceUtils {
    static buildHeaders(key: string): {
        Authorization: string;
        'Content-Type': string;
    };
    private static handleVerificationResult;
    static buildKeyVerificationDetails(): KeyVerificationDetails;
}
//# sourceMappingURL=huggingFaceUtils.d.ts.map