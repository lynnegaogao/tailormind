import { GenericInputButtonStyles } from '../../../../types/genericInputButton';
import { Positions } from '../buttons/styleAdjustments/inputButtonPositions';
import { DefinedButtonStateStyles } from '../../../../types/buttonInternal';
import { DropupStyles } from '../../../../types/dropupStyles';
import { InputButton } from '../buttons/inputButton';
type Styles = DefinedButtonStateStyles<GenericInputButtonStyles>;
export declare class Dropup extends InputButton<Styles> {
    private readonly _menu;
    readonly buttonContainer: HTMLElement;
    constructor(containerElement: HTMLElement, styles?: DropupStyles);
    private static createButtonElement;
    private createInnerElements;
    private createInnerElement;
    private static createSVGIconElement;
    private addClickEvent;
    private static createButtonContainer;
    addItem(buttonProps: InputButton): void;
    private addContainerEvents;
    static getPosition(positions: Positions, dropupStyles?: DropupStyles): import("../../../../types/button").ButtonPosition;
}
export {};
//# sourceMappingURL=dropup.d.ts.map