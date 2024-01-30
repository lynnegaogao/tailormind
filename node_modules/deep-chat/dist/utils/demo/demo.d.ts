import { ServiceIO, StreamHandlers } from '../../services/serviceIO';
import { Messages } from '../../views/chat/messages/messages';
export declare class Demo {
    static readonly URL = "deep-chat-demo";
    private static generateResponse;
    private static getCustomResponse;
    private static getResponse;
    static request(io: ServiceIO, messages: Messages): void;
    static requestStream(messages: Messages, sh: StreamHandlers): void;
}
//# sourceMappingURL=demo.d.ts.map