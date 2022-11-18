<wv:view>
    <wv:comp.column>
        <div class="row">
            <div class="ui column">
                <div style="margin-top: 12%;">
                    <wv:logo />
                </div>
            </div>
        </div>
                
        <div class="menu-buttons-box">
            <wv:comp.column class={menu-buttons}>
                <wv:comp.linkButton source={#!} iconName={fa fa-user} text={Admin} />
            </wv:comp.column>
            <wv:comp.column class={menu-buttons}>
                <wv:comp.linkButton source={#!} text={Get Started}/>
            </wv:comp.column>

            <wv:comp.column class={menu-buttons}>
                <wv:comp.linkButton source={#!} text={Documentation}/>
            </wv:comp.column>

            <wv:comp.column class={menu-buttons}>
                <wv:comp.linkButton source={#!} text={Downloads} iconName={fa fa-download}/>
            </wv:comp.column>

            <wv:comp.column class={menu-buttons}>
                <wv:comp.linkButton source={#!} text={Support}/>
            </wv:comp.column>
        </div>
    </wv:comp.column>

</wv:view>