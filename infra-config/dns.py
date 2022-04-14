import pulumi
import pulumi_cloudflare as cloudflare


class DNSManager(pulumi.ComponentResource):
    def __init__(self):
        self.config = pulumi.Config()
        zone_id = self.config.require("zone_id")
        self.zone = cloudflare.get_zone(zone_id=zone_id)

    def add_record(
        self,
        type: str,
        name: str,
        value: str,
        rs_name: str = None,
        proxied = False,
        opts: pulumi.ResourceOptions = None,
        *args,
        **kwargs,
    ):
        value = value.replace("@", self.zone.name)

        if not rs_name:
            rs_name = name.replace(".", "-")

        return cloudflare.Record(
            rs_name,
            type=type,
            name=name,
            value=value,
            zone_id=self.zone.id,
            opts=opts,
            proxied=proxied,
            *args,
            **kwargs,
        )

    def add_MX_record(self, value: str, priority: int):
        return self.add_record("MX", "@", value, priority=priority, proxied=False, rs_name=f"MX-{priority}")


class KlusterDNS(pulumi.ComponentResource):
    def __init__(self, name: str, ip: str):
        super().__init__(t="KlusterDNS", name=name)

        self.name = name
        self.dns_man = DNSManager()

        root = self.dns_man.add_record(
            type="A",
            name=f"{name}",
            value=ip,
            rs_name=f"{name}-root",
            opts=pulumi.ResourceOptions(parent=self),
        )

        wildcard = self.dns_man.add_record(
            type="CNAME",
            name=f"*.{name}",
            value=f"{name}.@",
            rs_name=f"{name}-wildcard",
            opts=pulumi.ResourceOptions(parent=self, depends_on=root),
        )

    def add_CNAME_pointer(self, name: str):
        """
            name: format `<appname>.<env>` or `<infra-app-name>`
        """
        assert "*" not in name
        assert name.count(".") <= 1

        return self.dns_man.add_record(
            type="CNAME",
            name=name,
            value=f"{self.name}.@",
            opts=pulumi.ResourceOptions(parent=self),
        )
