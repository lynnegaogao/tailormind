import { KeyVerificationDetails } from '../../../types/keyVerificationDetails';
export declare class CohereUtils {
    static buildHeaders(key: string): {
        Authorization: string;
        'Content-Type': string;
        accept: string;
    };
    private static handleVerificationResult;
    static buildKeyVerificationDetails(): KeyVerificationDetails;
}
//# sourceMappingURL=cohereUtils.d.ts.map