import { CustomStyle } from '../../types/styles';
export declare class WebComponentStyleUtils {
    private static readonly DEFAULT_COMPONENT_STYLE;
    static apply(style: string, shadowRoot: ShadowRoot | null): void;
    private static applyStyleSheet;
    private static addStyleElement;
    static applyDefaultStyleToComponent(style: CSSStyleDeclaration, chatStyle?: CustomStyle): void;
}
//# sourceMappingURL=webComponentStyleUtils.d.ts.map