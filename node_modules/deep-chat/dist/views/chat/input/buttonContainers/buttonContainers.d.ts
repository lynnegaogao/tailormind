import { ButtonPosition } from '../../../../types/button';
export type ButtonContainersT = readonly [HTMLDivElement, HTMLDivElement, HTMLDivElement, HTMLDivElement];
export declare class ButtonContainers {
    static create(): ButtonContainersT;
    static add(inputContainer: HTMLElement, buttonContainers: ButtonContainersT): void;
    private static getContainerIndex;
    static addButton(buttonContainers: ButtonContainersT, elementRef: HTMLElement, position: ButtonPosition): void;
}
//# sourceMappingURL=buttonContainers.d.ts.map