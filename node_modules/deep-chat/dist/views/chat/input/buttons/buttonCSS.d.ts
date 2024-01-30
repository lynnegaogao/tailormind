import { StatefulStyles } from '../../../../types/styles';
import { ButtonStyles } from '../../../../types/button';
export declare class ButtonCSS {
    static unsetAllCSS(button: HTMLElement, styles: ButtonStyles): void;
    static unsetActionCSS(button: HTMLElement, styles: ButtonStyles): void;
    static setElementsCSS(button: HTMLElement, styles: ButtonStyles, style: keyof StatefulStyles): void;
    static setElementCssUpToState(button: HTMLElement, styles: ButtonStyles, style: keyof StatefulStyles): void;
}
//# sourceMappingURL=buttonCSS.d.ts.map