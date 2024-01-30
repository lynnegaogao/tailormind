import { MessageContentI } from '../../types/messagesInternal';
import { DeepChat } from '../../deepChat';
export declare class FireEvents {
    static onNewMessage(deepChat: DeepChat, message: MessageContentI, isInitial: boolean): void;
    static onClearMessages(deepChat: DeepChat): void;
    static onRender(deepChat: DeepChat): void;
    static onError(deepChat: DeepChat, error: string): void;
}
//# sourceMappingURL=fireEvents.d.ts.map