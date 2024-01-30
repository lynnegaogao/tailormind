import { FileAttachmentsType } from '../../fileAttachments/fileAttachmentTypes/fileAttachmentsType';
import { ButtonContainersT } from '../../buttonContainers/buttonContainers';
import { DropupStyles } from '../../../../../types/dropupStyles';
import { BUTTON_TYPES } from '../../../../../types/buttonTypes';
import { ButtonPosition } from '../../../../../types/button';
import { InputButton } from '../inputButton';
export type Positions = {
    [key in ButtonPosition]: ButtonProps[];
};
type ButtonProps = {
    button: InputButton;
    buttonType?: BUTTON_TYPES;
    fileType?: FileAttachmentsType;
};
type Buttons = {
    [key in BUTTON_TYPES]?: ButtonProps;
};
export declare class InputButtonPositions {
    private static addToDropup;
    private static addToSideContainer;
    private static setPosition;
    private static createPositionsObj;
    private static generatePositions;
    static addButtons(buttonContainers: ButtonContainersT, buttons: Buttons, container: HTMLElement, dropupStyles?: DropupStyles): Positions;
}
export {};
//# sourceMappingURL=inputButtonPositions.d.ts.map