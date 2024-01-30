import { Messages } from '../../views/chat/messages/messages';
import { ServiceIO } from '../../services/serviceIO';
export declare class Websocket {
    static setup(io: ServiceIO): void;
    static createConnection(io: ServiceIO, messages: Messages): void;
    private static retryConnection;
    private static assignListeners;
    static sendWebsocket(io: ServiceIO, body: object, messages: Messages, stringifyBody?: boolean): Promise<void>;
    static canSendMessage(websocket: ServiceIO['websocket']): boolean;
    private static isWebSocket;
}
//# sourceMappingURL=websocket.d.ts.map