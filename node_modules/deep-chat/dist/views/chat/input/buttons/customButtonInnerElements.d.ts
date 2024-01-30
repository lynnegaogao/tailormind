import { ButtonInnerElements, ButtonStateStyles } from '../../../../types/buttonInternal';
export declare class CustomButtonInnerElements {
    private static createTextElement;
    private static createElement;
    static createCustomElement<T>(state: keyof T, customStyles?: ButtonStateStyles<T>): HTMLDivElement | SVGGraphicsElement | undefined;
    private static processElement;
    static createSpecificStateElement<T>(parentEl: HTMLElement, state: keyof T, customStyles?: ButtonStateStyles<T>): HTMLDivElement | SVGGraphicsElement | undefined;
    static create<T>(parentEl: HTMLElement, states: (keyof T)[], styles?: ButtonStateStyles<T>): ButtonInnerElements<T>;
}
//# sourceMappingURL=customButtonInnerElements.d.ts.map