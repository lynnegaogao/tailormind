import { HTMLClassUtilities } from '../../../../types/html';
import { MessagesBase } from '../messagesBase';
import { MessageElements } from '../messages';
export declare class HTMLDeepChatElements {
    private static applySuggestionEvent;
    static isElementTemporary(messageElements?: MessageElements): boolean;
    static doesElementContainDeepChatClass(element: HTMLElement): string | undefined;
    private static applyEvents;
    private static getProcessedStyles;
    static applyDeepChatUtilities(messages: MessagesBase, utilities: HTMLClassUtilities, element: HTMLElement): void;
}
//# sourceMappingURL=htmlDeepChatElements.d.ts.map