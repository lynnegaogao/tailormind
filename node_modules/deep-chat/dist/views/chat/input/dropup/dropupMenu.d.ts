import { DropupMenuStyles } from '../../../../types/dropupStyles';
import { InputButton } from '../buttons/inputButton';
export declare class DropupMenu {
    readonly elementRef: HTMLElement;
    private _isOpen;
    highlightedItem?: HTMLElement;
    private readonly _styles?;
    private clickEvent?;
    private keyDownEvent?;
    constructor(containerElement: HTMLElement, styles?: DropupMenuStyles);
    private static createElement;
    private open;
    close(): void;
    toggle(): void;
    addItem(inputButton: InputButton): void;
    private addWindowEvents;
    private windowClick;
    private windowKeyDown;
}
//# sourceMappingURL=dropupMenu.d.ts.map