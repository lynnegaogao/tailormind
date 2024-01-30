import { AttributeTypeConverter } from '../../types/typeConverters';
import { GenericObject } from '../../types/object';
export declare class InternalHTML extends HTMLElement {
    _waitingToRender_: boolean;
    _propUpdated_: boolean;
    static _attributes_: GenericObject<AttributeTypeConverter>;
    static _attributeToProperty_: GenericObject<string>;
    static get observedAttributes(): string[];
    constructor();
    private constructPropertyAccessors;
    attributeChangedCallback(attributeName: string, oldValue: string, newValue: string): void;
    onRender(): void;
}
//# sourceMappingURL=internalHTML.d.ts.map