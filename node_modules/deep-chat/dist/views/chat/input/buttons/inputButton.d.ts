import { ButtonPosition as ButtonPositionT } from '../../../../types/button';
import { StatefulStyles } from '../../../../types/styles';
import { ButtonStyles } from '../../../../types/button';
interface MouseState {
    state: keyof StatefulStyles;
}
export declare class InputButton<T extends {
    [key: string]: ButtonStyles;
} = {}> {
    readonly elementRef: HTMLElement;
    protected readonly _mouseState: MouseState;
    protected readonly _customStyles?: T;
    readonly position?: ButtonPositionT;
    readonly dropupText?: string;
    constructor(buttonElement: HTMLElement, position?: ButtonPositionT, customStyles?: T, dropupText?: string);
    private buttonMouseLeave;
    private buttonMouseEnter;
    private buttonMouseUp;
    private buttonMouseDown;
    private setEvents;
    unsetCustomStateStyles(unsetTypes: (keyof T)[]): void;
    reapplyStateStyle(setType: keyof T, unsetTypes?: (keyof T)[]): void;
}
export {};
//# sourceMappingURL=inputButton.d.ts.map