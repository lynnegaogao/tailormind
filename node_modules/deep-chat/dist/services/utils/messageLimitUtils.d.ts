import { MessageContentI } from '../../types/messagesInternal';
export declare class MessageLimitUtils {
    static getCharacterLimitMessages(messages: MessageContentI[], limit: number): MessageContentI[];
    private static getMaxMessages;
    static processMessages(messages: MessageContentI[], maxMessages?: number, totalMessagesMaxCharLength?: number): MessageContentI[];
}
//# sourceMappingURL=messageLimitUtils.d.ts.map