import { CustomStyle, StatefulStyles } from '../../types/styles';
export declare class StyleUtils {
    static unsetStyle(element: HTMLElement, style: CustomStyle): void;
    static unsetActivityCSSMouseStates(element: HTMLElement, statefulStyle: StatefulStyles): void;
    static unsetAllCSSMouseStates(element: HTMLElement, statefulStyle: StatefulStyles): void;
    static processStateful(styles: StatefulStyles, defHover: CustomStyle, defClick: CustomStyle): StatefulStyles;
    static mergeStatefulStyles(stylesArr: StatefulStyles[]): StatefulStyles;
    static overwriteDefaultWithAlreadyApplied(styles: StatefulStyles, element: HTMLElement): void;
    static applyToStyleIfNotDefined(cssDeclaration: CSSStyleDeclaration, source: CustomStyle): void;
}
//# sourceMappingURL=styleUtils.d.ts.map