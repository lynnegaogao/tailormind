import { MessageContentI } from '../../../types/messagesInternal';
import { MessageContent } from '../../../types/messages';
import { MessageElements } from './messages';
export declare class MessageUtils {
    static readonly AI_ROLE = "ai";
    static readonly USER_ROLE = "user";
    private static readonly EMPTY_MESSAGE_CLASS;
    static getLastElementsByClass(messagesElements: MessageElements[], classes: string[], avoidedClasses?: string[]): MessageElements | undefined;
    static getLastMessage(messages: MessageContentI[], role: string, content?: keyof Omit<MessageContent, 'role'>): MessageContentI | undefined;
    static getLastTextToElement(elemsToText: [MessageElements, string][], elems: MessageElements): [MessageElements, string] | undefined;
    static overwriteMessage(messages: MessageContentI[], messagesElements: MessageElements[], content: string, role: string, contentType: 'text' | 'html', className: string): MessageElements | undefined;
    static getRoleClass(role: string): string;
    static fillEmptyMessageElement(bubbleElement: HTMLElement, content: string): void;
    static unfillEmptyMessageElement(bubbleElement: HTMLElement, newContent: string): void;
    static getLastMessageBubbleElement(messagesEl: HTMLElement): Element | undefined;
    static getLastMessageElement(messagesEl: HTMLElement): Element;
}
//# sourceMappingURL=messageUtils.d.ts.map