import { Messages } from '../../views/chat/messages/messages';
import { RequestDetails } from '../../types/interceptors';
import { ServiceIO } from '../../services/serviceIO';
export interface IWebsocketHandler {
    isOpen: boolean;
    newUserMessage: {
        listener: (text: string) => void;
    };
}
export declare class CustomHandler {
    static request(io: ServiceIO, body: RequestDetails['body'], messages: Messages): Promise<void>;
    static stream(io: ServiceIO, body: RequestDetails['body'], messages: Messages): void;
    static websocket(io: ServiceIO, messages: Messages): void;
    private static generateOptionalSignals;
}
//# sourceMappingURL=customHandler.d.ts.map