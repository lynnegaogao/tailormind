import { Messages } from '../../views/chat/messages/messages';
import { ServiceIO } from '../../services/serviceIO';
export type HandleVerificationResult = (result: object, key: string, onSuccess: (key: string) => void, onFail: (message: string) => void) => void;
export declare class HTTPRequest {
    static request(io: ServiceIO, body: object, messages: Messages, stringifyBody?: boolean): Promise<void>;
    static executePollRequest(io: ServiceIO, url: string, requestInit: RequestInit, messages: Messages): void;
    static poll(io: ServiceIO, body: object, messages: Messages, stringifyBody?: boolean): Promise<void>;
    static verifyKey(key: string, url: string, headers: HeadersInit, method: string, onSuccess: (key: string) => void, onFail: (message: string) => void, onLoad: () => void, handleVerificationResult: HandleVerificationResult, body?: string): void;
}
//# sourceMappingURL=HTTPRequest.d.ts.map