import { MessageElementsStyles, MessageRoleStyles, MessageStyles } from '../../../types/messages';
import { CustomStyle } from '../../../types/styles';
import { MessageElements } from './messages';
export declare class MessageStyleUtils {
    static applyCustomStylesToElements(elements: MessageElements, isMedia: boolean, styles?: MessageElementsStyles): void;
    private static applySideStyles;
    private static isMessageSideStyles;
    static applyCustomStyles(messageStyles: MessageStyles, elements: MessageElements, role: string, media: boolean, otherStyles?: MessageRoleStyles | MessageElementsStyles): void;
    static extractParticularSharedStyles(specificStyles: (keyof CustomStyle)[], otherStyles?: MessageRoleStyles): MessageElementsStyles | undefined;
}
//# sourceMappingURL=messageStyleUtils.d.ts.map